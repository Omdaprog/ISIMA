from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from .forms import UploadFrom
from .models import PdfStore
# def homepage(request):
#     form = UploadFrom()
    
#     if request.method == "POST":
#         form = UploadFrom(request.POST or None, request.FILES or None)
#         if form.is_valid():
            
#             print(form.cleaned_data["title"])
#             print(form)
            




#     return render(request,"base.html")



class homepage(FormView):
    form_class = UploadFrom
    template_name = 'base.html'  # Replace with your template.
    # success_url = render(request,"base.html") # Replace with your URL or reverse().

    def post(self, request):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('image')
        if form.is_valid():
            for f in files:
                print(f)
                file_instance = PdfStore(resumes=f)
            return render(request,"base.html")
        else:
            return render(request,"base.html")












