import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from corporate_asset.models import Company, Employee, Asset, AssetLog
from corporate_asset.serializers import (CompanySerializer, EmployeeSerializer, AssetSerializer,
                                         AssetLogSerializer)

# Create your views here.

class CompanyList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        company = Company.objects.all()
        serializer = CompanySerializer(company, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        '''
        We recieve new company data from a post request. The data we expect are
        name, contact_number, email, address. We pass the data to the serializer
        and validate it. Then we use the serializer save() function to to create
        a new Company Object and save it to the database.
        '''
        serializer = CompanySerializer(data=request.data)           
                                                                    
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        

class EmployeeList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        '''
        We recieve new employee data from a post request. The data we expect are
        name, company, address, contact_number, lent_assets. We pass the data to the serializer
        and validate it. Then we use the serializer save() function to to create
        a new Employee Object and save it to the database.
        '''
        serializer = EmployeeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        

class AssetList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        asset = Asset.objects.all()
        serializer = AssetSerializer(asset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        '''
        We recieve new asset data from a post request. The data we expect are
        name, company, type, price, serial_number. We pass the data to the serializer
        and validate it. Then we use the serializer save() function to to create
        a new Asset Object and save it to the database.
        '''
        serializer = AssetSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class AssetDetail(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        request_data = request.data
        company = request_data.get('company', '')
        lent_to = request_data.get('lent_to', '')
        condition_lent = request_data.get('condition_lent', '')
        condition_returned = request_data.get('condition_returned', '')
        return_by = request_data.get('return_by', '')
        returned_at = request_data.get('returned_at', '')
        
        if returned_at != '':                                               # If we have a value for returned_at that means the
                                                                            # asset has been returned by the employee
            request_data['lent_to'] = None                                  # We update the 'lent_to' of the asset with null value since the asset has been returned

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

                AssetLog.objects.create(company=company,                        # We create an asset log when the asset has been returned
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
        asset_logs = AssetLog.objects.all()
        serializer = AssetLogSerializer(asset_logs, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)            