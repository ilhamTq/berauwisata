from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import Artikel

class ArtikelForms(forms.ModelForm):
    class Meta:
        model = Artikel
        fields = ('judul', 'isi', 'kategori', 'thumbnail')
        widgets = {
            "judul" : forms.TextInput(
                attrs={
                    'class':'form-control',
                    'type':'text',
                    'placeholder':"Judul Artikel",
                    'required':True,
                }
            ),
            "isi" : forms.Textarea(
                attrs={
                    'class':'form-control',
                    'cols':'30',
                    'rows':'10',
                    'required':True
                }
            ),
            "kategori" : forms.Select(
                attrs={
                    'class':'selectpicker',
                    'type':'text',
                    'placeholder':'Judul',
                    'required':True,
                    'data-style':'btn btn-success btn-block',
                    'title':'Pilih Kategori'
                }
            ),
            # "thumbnail" : forms.ImageField(upload_to)
        }
        