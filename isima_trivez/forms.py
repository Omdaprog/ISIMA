from django.forms import ModelForm
from .models import PdfStore 
from django import forms

class UploadForm(ModelForm):
    title = forms.CharField()
    matire = forms.CharField()
    degree = forms.CharField()
    description = forms.CharField()
    slug = forms.CharField()
    image = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    

    class Meta: 
        model = PdfStore  
        fields = ['title','matire','degree','description','slug','image']


    

#         widgets = {
#             'image': forms.ClearableFileInput(attrs={'multiple': True}) 
#         }