from django.urls import path
from corporate_asset import views

urlpatterns = [
    path('company', views.CompanyList.as_view(), name='company'),
    path('company-admin', views.CompanyAdminList.as_view(), name='company_admin'),
    path('employee', views.EmployeeList.as_view(), name='employee'),
    path('asset', views.AssetList.as_view(), name='asset'),
    path('asset-detail', views.AssetDetail.as_view(), name='asset_detail'),
    path('asset-log', views.AssetLogList.as_view(), name='asset_log')
]