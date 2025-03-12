from django import forms
from django.forms.widgets import NumberInput

from . models import food_order,Reservations
class Kili_order(forms.ModelForm):
    class Meta:
        model = food_order
        fields =['first_name', 'last_name','address',]


class Res_order(forms.ModelForm):
    class Meta:
        model = Reservations
        fields =['first_name', 'last_name', 'date', 'phone_num']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'})}