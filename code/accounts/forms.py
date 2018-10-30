from .models import Myproducts
from django import forms

class MyproductsForm(forms.ModelForm):
    Product = forms.ModelMultipleChoiceField(
            widget=forms.CheckboxSelectMultiple, queryset = Myproducts.objects.all()
            )
    class Meta:
        model  = Myproducts
        fields = ['my_all_products']
