from . models import Product
from django import forms

class ProductCreateForm(forms.ModelForm):
    
    class Meta:
        Product
