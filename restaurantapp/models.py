from django.db import models
from django.contrib.auth.models import User
from adminside.models import Product
# Create your models here.
class Udetails(models.Model):
    phone=models.BigIntegerField()
    city = models.CharField(max_length=50)
    uid = models.ForeignKey(User,on_delete=models.CASCADE)
    class Meta:
        db_table='userdetails'

class Booktable(models.Model):
    name = models.CharField(max_length=50)
    phone = models.BigIntegerField()
    numberofper = models.CharField(max_length=5)
    date = models.DateField()
    email = models.EmailField()
    uid = models.ForeignKey(User,on_delete=models.CASCADE)
    class Meta:
        db_table = 'booktable'

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    class Meta:
        db_table='cart'

class Cart_itmes(models.Model):
    cartid = models.ForeignKey(Cart,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    itemTotal = models.IntegerField(default=0)
    itemPrice = models.IntegerField(default=0)
    def save(self, *args, **kwargs):
        # Calculate subtotal based on quantity and item price
        pPrice = Product.objects.values('price').filter(pk=self.product.id)
        self.itemPrice = pPrice[0]['price']
        self.itemTotal = self.quantity * self.itemPrice
        super().save(*args, **kwargs)

    class Meta:
        db_table='cartitemss'
