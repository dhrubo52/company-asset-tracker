from rest_framework import serializers
from corporate_asset.models import Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name', 'contact_number', 'email', 'address']