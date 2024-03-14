from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=50)
    contact_number = models.IntegerField(max_length=30)
    email = models.EmailField()
    address = models.TextField()