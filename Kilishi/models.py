from django.db import models
from django.utils import timezone
from cloudinary.models import CloudinaryField
# Create your models here.
class kilishi_order(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date = models.DateField()
    phone_num = models.CharField(max_length=15)
    address = models.CharField(max_length=400)
    size = models.IntegerField(default=0)
    def __str__(self):
        return self.first_name +'  '+ self.last_name+'  '+self.size+'  '+self.address

class products(models.Model):
    product_name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    image = CloudinaryField('image')
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
