from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=50)
    contact_number = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()


class Employee(models.Model):
    name = models.CharField(max_length=50)
    company = models.ForeignKey('Company', related_name='employees', on_delete=models.CASCADE)
    address = models.TextField()
    contact_number = models.IntegerField()


class Asset(models.Model):
    company = models.ForeignKey('Company', related_name='assets', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=20, null=True)
    price = models.CharField(max_length=15, null=True)                           # Price of the asset
    serial_number = models.CharField(max_length=50)                              # Serial number of the asset
    lent_to = models.ForeignKey('Employee', related_name='lent_assets', on_delete=models.SET_NULL, null=True, blank=True)      # The employee the asset was lent to
    condition_lent = models.TextField(null=True, blank=True)                     # Condition of the asset at the time of lending to the employee
    condition_returned = models.TextField(null=True, blank=True)                 # Condition of the asset at the time of being returned by the employee
    return_by = models.DateField(null=True, blank=True)                          # The date by which the employee has to return the asset
    returned_at = models.DateField(null=True, blank=True)                        # The actual date the asset was returned


class AssetLog(models.Model):
    company = models.ForeignKey('Company', related_name='asset_log', on_delete=models.CASCADE)
    lent_to = models.ForeignKey('Employee', related_name='asset_log', on_delete=models.SET_NULL, null=True)
    condition_lent = models.TextField()
    condition_returned = models.TextField()
    return_by = models.DateField()
    returned_at = models.DateField()