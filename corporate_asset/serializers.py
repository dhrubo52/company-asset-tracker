from rest_framework import serializers
from corporate_asset.models import Company, Employee

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'contact_number', 'email', 'address']


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'company', 'age', 'address', 'contact_number', 'lent_assets']