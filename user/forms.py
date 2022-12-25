from django import forms
from .models import Biodata
from django.contrib.auth.models import User

class UserForms(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        widgets = {
            "first_name" : forms.TextInput(
                attrs={
                    'class':'form-control',
                    'type':'text',
                    'placeholder':"First Name",
                    'required':True,
                }
            ),
            "last_name" : forms.TextInput(
                attrs={
                    'class':'form-control',
                    'type':'text',
                    'placeholder':"Last Name",
                    'required':True,
                }
            ),
            "email" : forms.TextInput(
                attrs={
                    'class':'form-control',
                    'type':'text',
                    'placeholder':"Email",
                    'required':True,
                }
            ),
        }
        
class BiodataForms(forms.ModelForm):
    class Meta:
        model = Biodata
        fields = ('alamat', 'telp')
        widgets = {
            "alamat" : forms.Textarea(
                attrs={
                    'class':'form-control',
                    'type':'text',
                    'placeholder':"Address",
                    'required':True,
                }
            ),
            "telp" : forms.TextInput(
                attrs={
                    'class':'form-control',
                    'type':'text',
                    'placeholder':"Phone",
                    'required':True,
                }
            ),
        }