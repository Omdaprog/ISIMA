from django.shortcuts import render, redirect
from .forms import UploadFrom
def homepage(request):
    form = UploadFrom()
    if request.method == "POST":
        form = UploadFrom(request.POST or None, request.FILES or None)
        if form.is_valid():
            print(form.cleaned_data["title"])
            print(form.cleaned_data["image"])
            




    return render(request,"base.html")
