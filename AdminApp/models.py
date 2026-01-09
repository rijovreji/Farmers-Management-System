from django.db import models

# Create your models here.
class Farmers_Db(models.Model):
    f_name=models.CharField(max_length=50,null=True,blank=True)
    f_email=models.EmailField(max_length=100,null=True,blank=True)
    f_number=models.IntegerField(null=True,blank=True)
    f_password=models.CharField(max_length=50,null=True,blank=True)

class Seeds_Db(models.Model):
    seeds_name=models.CharField(max_length=100,null=True,blank=True)
    seeds_type=models.CharField(max_length=100,null=True,blank=True)
    seeds_quantity=models.IntegerField(null=True,blank=True)
    seeds_price=models.IntegerField(null=True,blank=True)
    seeds_image=models.ImageField(upload_to="Seeds_Image",null=True,blank=True)
    seeds_description=models.CharField(max_length=300,null=True,blank=True)

class Farming_Tools_Db(models.Model):
    tool_name=models.CharField(max_length=100,null=True,blank=True)
    tool_type=models.CharField(max_length=100,null=True,blank=True)
    tool_quantity=models.IntegerField(null=True,blank=True)
    tool_price=models.IntegerField(null=True,blank=True)
    tool_image=models.ImageField(upload_to="Tools_image",null=True,blank=True)
    tool_description=models.CharField(max_length=250,null=True,blank=True)







