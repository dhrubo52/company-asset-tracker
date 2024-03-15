from rest_framework import serializers
from corporate_asset.models import Company, CompanyAdmin, Employee, Asset, AssetLog

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'contact_number', 'email', 'address', 'employees', 'assets']


class CompanyAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyAdmin
        fields = ['id', 'user', 'company']


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'company', 'address', 'contact_number', 'lent_assets']


class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = ['id', 'company', 'name', 'type', 'price', 'serial_number', 'lent_to', 'condition_lent',
                  'condition_returned', 'return_by', 'returned_at']
        

class AssetLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetLog
        fields = ['id', 'company', 'lent_to', 'condition_lent', 'condition_returned', 'return_by',
                  'returned_at']