from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from corporate_asset.models import Company, Employee
from corporate_asset.serializers import CompanySerializer, EmployeeSerializer

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
        serializer = EmployeeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        