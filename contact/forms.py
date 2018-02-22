from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    #date = forms.DateTimeField(widget=forms.HiddenInput())
    class Meta:
        model = Contact
        fields = '__all__'
        exclude =['date']


