from django.contrib import admin
from . models import food_order, products,Reservations
# Register your models here.
admin.site.register(food_order)
admin.site.register(products)
admin.site.register(Reservations)