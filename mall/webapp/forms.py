from django import forms
from django.forms import widgets

CHOICES = [('other', 'разное'), ('electronics', 'электроника'), ('clothes', 'одежда'), ('for_home', 'Для дома'),
           ('sports', 'спорт')]

class StufsForm(forms.Form):
    stuf = forms.CharField(max_length=100, required=True, label="Stuf")
    description = forms.CharField(max_length=2000, required=True, label="Description")
    categories = forms.ChoiceField(required=True, choices=CHOICES,
                                  label="categories")
    remainder = forms.IntegerField(min_value=1, required=True, label="remainder")
    price = forms.DecimalField(required=True, max_digits=7, decimal_places=2, label="price")