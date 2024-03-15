from django.contrib import admin
from .models import Company, CompanyAdmin, Employee, Asset, AssetLog

# Register your models here.
admin.site.register(Company)
admin.site.register(CompanyAdmin)
admin.site.register(Employee)
admin.site.register(Asset)
admin.site.register(AssetLog)