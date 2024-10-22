from django.db import models
from adminside.models import Product
from manager.models import Tables,Waiter
# Create your models here.
class Waitercart(models.Model):
    wid = models.ForeignKey(Waiter,on_delete=models.CASCADE,blank=True,null=True)
    tableno = models.ForeignKey(Tables,on_delete=models.CASCADE,default=1)
    pid = models.ForeignKey(Product,on_delete=models.CASCADE)
    pquantity = models.IntegerField(default=0)
    class Meta:
        db_table = 'waitercart'

class Order(models.Model):
    wid = models.ForeignKey(Waiter,on_delete=models.CASCADE,blank=True,null=True)
    tableno = models.ForeignKey(Tables,on_delete=models.CASCADE)
    productname = models.CharField(max_length=200)
    pquantity = models.IntegerField(default=0)
    status = models.CharField(max_length=50,default='pending')
    class Meta:
        db_table='order'

class TempOrder(models.Model):
    wid = models.ForeignKey(Waiter,on_delete=models.CASCADE,blank=True,null=True)
    tableno = models.ForeignKey(Tables,on_delete=models.CASCADE)
    productname = models.CharField(max_length=200)
    pquantity = models.IntegerField(default=0)
    status = models.CharField(max_length=50,default='pending')
    class Meta:
        db_table='temporder'