from django import forms
from shop.models import Services
from customercorner.models import Product

class ServiceCreateForm(forms.ModelForm):
    Product = forms.ModelMultipleChoiceField(
            widget=forms.CheckboxSelectMultiple, queryset = Product.objects.all()
            )
    class Meta:
        model  = Services
        fields = ['Company_Name' ,'Service_name' ,'Price', 'Product','Description','images']
