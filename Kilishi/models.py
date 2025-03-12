from django.db import models
from django.utils import timezone

# Create your models here.
class food_order(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_num = models.CharField(max_length=15)
    address = models.CharField(max_length=400)
    def __str__(self):
        return self.first_name +'  '+ self.last_name+' '+self.address

class products(models.Model):
    product_name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/')
    desc = models.TextField(default=None, null=True, blank=True)
    def __str__(self):
        return f"{self.product_name}"

class Cart(models.Model):
    product = models.ForeignKey(products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    

class Reservations(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date = models.DateTimeField(default=timezone.now)
    phone_num = models.CharField(max_length=15)
    def __str__(self):
        return self.first_name +' '+ self.last_name 
