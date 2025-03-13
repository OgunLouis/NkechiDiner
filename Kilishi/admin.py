from django.contrib import admin
from . models import kilishi_order, products,Reservations
# Register your models here.
admin.site.register(kilishi_order)
admin.site.register(products)
admin.site.register(Reservations)