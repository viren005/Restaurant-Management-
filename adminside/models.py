from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    categoryname = models.CharField(max_length=25)
    class Meta:
        db_table='category'

class Product(models.Model):
    pname = models.CharField(max_length=25)
    description = models.CharField(max_length=500)
    price = models.IntegerField()
    pcid= models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.URLField()
    class Meta:
        db_table = 'product'    

class Banner(models.Model):
    bannername = models.CharField(max_length=100)
    bannerdescription = models.CharField(max_length=1000)
    class Meta:
        db_table='banner'

class Manager(models.Model):
    managername = models.CharField(max_length=50)
    manageremail=models.CharField(max_length=50)
    managerpassword = models.CharField(max_length=200)
    last_login = models.DateField(default=datetime.now())
    class Meta:
        db_table='manager'