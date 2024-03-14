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