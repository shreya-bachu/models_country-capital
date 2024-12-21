from django.db import models

class Country(models.Model):
    countryID=models.IntegerField(primary_key=True)
    countryName=models.CharField(max_length=100)


class Capital(models.Model):
    capitalID=models.IntegerField(primary_key=True)
    capitalName=models.CharField(max_length=100)
    countryID=models.OneToOneField(Country,on_delete=models.CASCADE)


    
    
# Create your models here.
