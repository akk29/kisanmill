from django import forms
from .models import Bond

class BondCreateForm(forms.ModelForm):
        Product = forms.ModelMultipleChoiceField(
                widget=forms.CheckboxSelectMultiple, queryset = Product.objects.all()
                )
        class Meta:
            model  = Services
            fields = ['Company_Name' ,'Service_name' ,'Price', 'Product','Description','images']
