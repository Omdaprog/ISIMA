from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from .forms import  UploadImages, UploadForm
from .models import PdfStore, PdfImages
# def homepage(request):
#     form = UploadFrom()
    
#     if request.method == "POST":
#         form = UploadFrom(request.POST or None, request.FILES or None)
#         if form.is_valid():
            
#             print(form.cleaned_data["title"])
#             print(form)
            




#     return render(request,"base.html")



class homepage(FormView):
    form_class = UploadForm
    template_name = 'base.html'
     # Replace with your template.
    success_url = '/' # Replace with your URL or reverse().

    def form_valid(self, form):
        print('form saved')
        form.save()
        return super().form_valid(form)



    # def Post(self, request, *args, **kwargs):
    #     print("post work fine")
    #     form_class= self.get_form_class()
    #     form = self.get_form(form_class)
    #     files = request.FILES.getlist('image')
    #     if form.is_valid():
    #         for f in files: 
    #             print(f)
    #             f.save()
    #         return render(request,"base.html")  
    #     else:
    #         return render(request,"base.html")





    # def post(self, request):
        
    #     form_class = self.get_form_class()
    #     form = self.get_form(form_class)
    #     files = request.FILES.getlist('image')
    #     if form.is_valid():
    #         pdfstore = form.save(commit=False)
    #         pdfstore.save()
    #         for f in files:
    #             print(f)
    #             file_instance = PdfImages(image=f)
    #             file_instance.save() # https://github.com/Bhagyalakshmi18/Resume_django/blob/master/web_app/views.py
    #         print('sucsessfuly posted')
    #         return render(request,"base.html")
    #     else:
    #         return render(request,"base.html")












