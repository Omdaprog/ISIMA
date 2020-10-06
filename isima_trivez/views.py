from django.shortcuts import render, redirect, get_object_or_404
from .forms import Post_info_form, Upload_image_form, SearchForm
from .models import Post,UploadImages
from django.views.generic import ListView, View


class HomeView(ListView):
    template_name = 'PostPage.html'
    model = Post


    def get(self, *args, **kwargs):
        form = SearchForm()
        context = {'form':form}
        return render(self.request,"HomePage.html",context)
    def get_queryset(self):
        # Must get data with forms.ChoiceField() , create choise dictionary, but .... it's too long  
        Class = self.request.POST.get('Class')
        matiere = self.request.POST.get('matiere')
        cour_td = self.request.POST.get('cour_td')

        # print(Class + matiere +cour_td)
        data = Class + matiere +cour_td
        object_list =self.model.objects.filter(matire=matiere,degree=Class )
        return object_list 
    def post(self, *args, **kwargs):
        data = self.get_queryset()
        context = {'data':data}
        return render(self.request, 'PostPage.html', context)


#TODO:Post the posts that match with value searched 






def upload_post(request):
    
    if request.method == 'POST':
        post_info = Post_info_form(request.POST)
        # print(post_info)
        images_uploded = Upload_image_form(request.POST or None, request.FILES or None)
        image = request.FILES.getlist('image')
        print(image)

        if post_info.is_valid() and images_uploded.is_valid():
            post = post_info.save(commit=False)
            post.save()
            for f in image:
                
                photos = UploadImages(post=post, image = f)
                print(f)
                photos.save()
    else:
        post_info = Post_info_form()
        images_uploded = Upload_image_form()
    context = {
        'post_info': post_info,
        'images_uploded': images_uploded
    }
    return render(request, 'PostDetail.html', context)











