from django import forms
from django.forms.widgets import NumberInput

from . models import kilishi_order,Reservations
class Kili_order(forms.ModelForm):
    class Meta:
        model = kilishi_order
        fields =['first_name', 'last_name', 'date','address','size']


class Res_order(forms.ModelForm):
    class Meta:
        model = Reservations
        fields =['first_name', 'last_name', 'date', 'phone_num']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'})}