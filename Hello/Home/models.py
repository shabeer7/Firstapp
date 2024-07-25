from django.db import models

# Create your models here.

class contact(models.Model):
    Name=models.CharField(max_length=50)
    Number=models.IntegerField(max_length=50)
    Email=models.EmailField(max_length=254)
    Password=models.CharField(max_length=50)
