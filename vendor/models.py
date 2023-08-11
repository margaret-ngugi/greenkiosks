from django.db import models

# Create your models here.
class Vendor(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    userName = models.CharField(max_length=50)
    password = models.CharField(max_length=8) 
    date_updated = models.DateTimeField(auto_now=True)

    
