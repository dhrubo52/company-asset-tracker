from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth.models import User

from corporate_asset.models import Company, Employee, Asset, AssetLog, CompanyAdmin
from corporate_asset.serializers import (CompanySerializer, CompanyAdminSerializer, EmployeeSerializer,
                                        AssetSerializer, AssetLogSerializer)

# Create your views here.

class CompanyList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        '''
        First we check if the user is superuser. Only superuser is allowed to get the list of Companies.
        If user is not superuser then we return response with unauthorized status.
        '''
        if not request.user.is_superuser:                                           
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        
        company = Company.objects.all()
        serializer = CompanySerializer(company, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        '''
        We recieve new company data from a post request. The data we expect are
        name, contact_number, email, address. We pass the data to the serializer
        and validate it. Then we use the serializer save() function to to create
        a new Company Object and save it to the database.

        First we check if the user is superuser. Only superuser is allowed to create new Company.
        If user is not superuser then we return response with unauthorized status.
        '''
        if not request.user.is_superuser:                                           
            return Response(status=status.HTTP_401_UNAUTHORIZED)
            
        serializer = CompanySerializer(data=request.data)           
                                                                    
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompanyAdminList(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        '''
        First we check if the user is superuser. Only superuser is allowed to create new Company.
        If user is not superuser then we return response with unauthorized status.
        '''
        if not request.user.is_superuser:                                           
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        username = request.data.get('username', '')
        password = request.data.get('password', '')
        first_name = request.data.get('first_name', '')
        last_name = request.data.get('last_name', '')
        email = request.data.get('email', '')
        company = request.data.get('company', '')

        if username=='' or password=='' or first_name=='' or last_name=='' or email=='' or company=='':
            return Response(status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username,
                                        password=password,
                                        email=email,
                                        first_name=first_name,
                                        last_name=last_name)
        
        user.is_staff = False
        user.is_superuser = False
        user.save()

        try:
            company = Company.objects.get(id=company)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        company_admin = CompanyAdmin.objects.create(user=user, company=company)
        serializer = CompanyAdminSerializer(company_admin)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class EmployeeList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        '''
        Here we get a list of  all the employees for a given company. 
        First we check if the user is a superuser. Superuser is allowed to 
        get the list of all employees for any company. If the user is not a superuser
        then check if the user is from the same company as the request company, if not then
        we return response with unauthorized status.
        '''
        company = request.GET.get('company', '')

        if not request.user.is_superuser:                                           
            user_company = str(request.user.company_admin.company.id)

            if user_company != company:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
        
        employee = Employee.objects.filter(company=company)
        serializer = EmployeeSerializer(employee, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        '''
        We recieve new employee data from a post request. The data we expect are
        name, company, address, contact_number, lent_assets. We pass the data to the serializer
        and validate it. Then we use the serializer save() function to to create
        a new Employee Object and save it to the database.

        First we check if the user is superuser. Superuser is allowed to create new Employee.
        If user is not superuser then we check if the user is from the company where the employee
        is being created, if not then we return response with unauthorized status.
        '''
        if not request.user.is_superuser:                                           
            user_company = str(request.user.company_admin.company.id)

            if user_company != request.data.get('company', ''):
                return Response(status=status.HTTP_401_UNAUTHORIZED)

        serializer = EmployeeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        

class AssetList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        '''
        Here we get a list of  all the assets for a given company. 
        First we check if the user is a superuser. Superuser is allowed to 
        get the list of all assets for any company. If the user is not a superuser
        then we check if the user is from the same company as the request company, if not then
        we return response with unauthorized status.
        '''
        company = request.GET.get('company', '')

        if not request.user.is_superuser:                                           
            user_company = str(request.user.company_admin.company.id)

            if user_company != company:
                return Response(status=status.HTTP_401_UNAUTHORIZED)

        asset = Asset.objects.filter(company=company)
        serializer = AssetSerializer(asset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        '''
        We recieve new asset data from a post request. The data we expect are
        name, company, type, price, serial_number. We pass the data to the serializer
        and validate it. Then we use the serializer save() function to to create
        a new Asset Object and save it to the database.

        First we check if the user is superuser. Superuser is allowed to create new Asset.
        If user is not superuser then we check if the user is from the company where the Asset
        is being created, if not then we return response with unauthorized status.
        '''
        if not request.user.is_superuser:                                           
            user_company = str(request.user.company_admin.company.id)

            if user_company != request.data.get('company', ''):
                return Response(status=status.HTTP_401_UNAUTHORIZED)
        
        serializer = AssetSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class AssetDetail(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        '''
        Here we update the status of asset. We update to whom an asset was lent to, what the condition was
        at the time of lending, in what condition the asset was returned, when the asset is to be returned
        and when the asset was actually returned.

        First we check if the user is a superuser. We will not allow superusers to
        update asset status. Only company admin users can change status of assets in their own company.
        If the user is not superuser then we check if the user is from the same company as the request 
        company, if not then we return response with unauthorized status.
        '''
        request_data = request.data
        company = request_data.get('company', '')
        lent_to = request_data.get('lent_to', '')
        condition_lent = request_data.get('condition_lent', '')
        condition_returned = request_data.get('condition_returned', '')
        return_by = request_data.get('return_by', '')
        returned_at = request_data.get('returned_at', '')

        if request.user.is_superuser:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        else:
            user_company = str(request.user.company_admin.company.id)

            if user_company != company:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
        
        if returned_at != '':                                                  # If we have a value for returned_at that means the
                                                                               # asset has been returned by the employee
            request_data['lent_to'] = None                                     # We update the 'lent_to' property of the asset with null value since the asset has been returned

        try:
            old_data = Asset.objects.get(id=request_data.get('id', ''))
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = AssetSerializer(old_data, data=request_data)
        
        if serializer.is_valid():
            serializer.save()

            if returned_at != '':                                               # If we have a value for returned_at that means the
                try:                                                            # asset has been returned by the employee
                    company = Company.objects.get(id=company)
                    lent_to = Employee.objects.get(id=lent_to)
                except:
                    return Response(status=status.HTTP_400_BAD_REQUEST)

                new_data = Asset.objects.get(id=request_data.get('id', ''))

                AssetLog.objects.create(asset=new_data,                         # We create an asset log when the asset has been returned
                                        company=company,                        
                                        lent_to=lent_to, 
                                        condition_lent=condition_lent,
                                        condition_returned=condition_returned,
                                        return_by=return_by,
                                        returned_at=returned_at)

            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            print(serializer.errors)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        

class AssetLogList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        '''
        Here we get a list of  all the asset logs for a given company. 
        First we check if the user is a superuser. Superuser is allowed to 
        get the list of all asset logs for any company. If the user is not a superuser
        then check if the user is from the same company as the request company, if not then
        we return response with unauthorized status.
        '''
        company = request.GET.get('company', '')

        if not request.user.is_superuser:                                           
            user_company = str(request.user.company_admin.company.id)

            if user_company != company:
                return Response(status=status.HTTP_401_UNAUTHORIZED)

        asset_logs = AssetLog.objects.filter(company=company)
        serializer = AssetLogSerializer(asset_logs, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)            