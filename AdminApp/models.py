from django.db import models

# Create your models here.
class Farmers_Db(models.Model):
    f_name=models.CharField(max_length=50,null=True,blank=True)
    f_email=models.EmailField(max_length=100,null=True,blank=True)
    f_number=models.IntegerField(null=True,blank=True)
    f_password=models.CharField(max_length=50,null=True,blank=True)


