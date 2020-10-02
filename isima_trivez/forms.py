from django.forms import ModelForm
from .models import Post , UploadImages
from django import forms

class Post_info_form(ModelForm):
    title = forms.CharField()
    matire = forms.CharField()
    degree = forms.CharField()
    description = forms.CharField()
    slug = forms.CharField()
    

    

    class Meta: 
        model = Post  
        fields = ['title','matire','degree','description','slug']


    

class Upload_image_form(forms.Form):   
    image = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    