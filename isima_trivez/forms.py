from django import forms

class UploadFrom(forms.Form):
    # title = forms.CharField()
    # matiere = forms.CharField()
    # degree = forms.CharField()
    # description = forms.TextInput()
    image = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))