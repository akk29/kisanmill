from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    First_seen = forms.DateField(widget=forms.TextInput(attrs=
                                {
                                    'class':'datepicker'
                                }))
    class Meta:
        model = Message
        fields = ['title','effected_crop','Description', 'Images','First_seen']
