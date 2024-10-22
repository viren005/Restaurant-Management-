import datetime
from django.utils.timezone import now
from datetime import datetime
from django.db import models

# Create your models here.
class Waiter(models.Model):
    waitername = models.CharField(max_length=50)
    waiteremail=models.CharField(max_length=50)
    waiterpassword = models.CharField(max_length=200)
    last_login = models.DateField(default=datetime.now())
    is_authenticated = models.BooleanField(default=False)
    class Meta:
        db_table='waiter'

class Chef(models.Model):
    chefname = models.CharField(max_length=50)
    chefemail=models.CharField(max_length=50)
    chefpassword = models.CharField(max_length=200)
    last_login = models.DateField(default=now())
    class Meta:
        db_table='chef'

class Tables(models.Model):
    tableNo = models.IntegerField()
    tableSize = models.IntegerField()
    isActive = models.CharField(max_length=20,default='close')
    class Meta:
        db_table = 'tables'
