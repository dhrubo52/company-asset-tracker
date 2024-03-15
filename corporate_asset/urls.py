from django.urls import path
from corporate_asset import views

urlpatterns = [
    path('company', views.CompanyList.as_view()),
    path('employee', views.EmployeeList.as_view()),
    path('asset', views.AssetList.as_view()),
    path('asset-detail', views.AssetDetail.as_view())
]