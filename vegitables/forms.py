from django import forms
from .models import Vegitable, Fruit

class VegitableForm(forms.ModelForm):
    class Meta:
        model = Vegitable
        fields = ['name', 'description', 'typee', 'price', 'count', 'mavsum']
        
        
class FruitForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = ['name', 'description', 'typee', 'price', 'count', 'mavsum']