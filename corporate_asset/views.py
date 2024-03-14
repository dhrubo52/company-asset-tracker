from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from corporate_asset.models import Company
from corporate_asset.serializers import CompanySerializer

# Create your views here.

class CompanyList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        company = Company.objects.all()
        serializer = CompanySerializer(company, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)