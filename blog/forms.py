from django import forms
from .models import *



class PostCreate(forms.ModelForm):
    title = forms.CharField(label="Τίτλος 'Αθρου", widget=forms.TextInput(attrs={'onkeyup':"myTitle()",}))
    lead_content = forms.CharField(label='Πρώτα Σχόλια', widget=forms.Textarea(attrs={'onkeyup':"myLeadCon()",}))
    content = forms.CharField(label='Βασικό Κείμενο', widget=forms.Textarea(attrs={'onkeyup':"myCon()",}))
    #content = forms.CharField(label='Βασικό Κείμενο', widget=FroalaEditor(attrs={'onkeyup':"myCon()",}))
    #user = forms.ChoiceField(widget=forms.HiddenInput())
    #publish = forms.DateTimeField(widget=forms.DateTimeField())

    class Meta:
        model=Post
        fields = '__all__'
        exclude=['publish','user']

class PostTagForm(forms.ModelForm):

    class Meta:
        model = PostTags
        fields= '__all__'

class PostCategoryForm(forms.ModelForm):

    class Meta:
        model = PostCategory
        fields = '__all__'