from django.shortcuts import render, redirect
from .forms import Post_info_form, Upload_image_form, SearchForm
from .models import Post,UploadImages
from django.views.generic import ListView, View


class HomeView(View):
    
    def get(self, *args, **kwargs):
        form = SearchForm()
        context = {'form':form}
        return render(self.request,"HomePage.html",context)
    def post(self, *args, **kwargs):
        # Must get data with forms.ChoiceField() , create choise dictionary, but it's too long  
        Class = self.request.POST.get('Class')
        matiere = self.request.POST.get('matiere')
        cour_td = self.request.POST.get('cour_td')

        print(Class + matiere +cour_td)
        
        return redirect("isima_trivez:new_post")


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











