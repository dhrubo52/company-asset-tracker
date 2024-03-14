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
    age = models.IntegerField()
    address = models.TextField()
    contact_number = models.IntegerField()


class Asset(models.Model):
    company = models.ForeignKey('Company', related_name='assets', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=20, null=True)
    price = models.IntegerField(null=True)               # Price of the asset
    serial_number = models.CharField(max_length=50)      # Serial number of the asset
    lent_to = models.ForeignKey('Employee', related_name='lent_devices', on_delete=models.SET_NULL, null=True)      # The employee the asset was lent to
    condition_lent = models.TextField(null=True)         # Condition of the asset at the time of lending to the employee
    condition_returned = models.TextField(null=True)     # Condition of the asset at the time of being returned by the employee
    return_by = models.DateField(null=True)              # The date by which the employee has to return the asset
    returned_at = models.DateField(null=True)            # The actual date the asset was returned