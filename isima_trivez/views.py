from django.shortcuts import render, redirect, get_object_or_404
from .forms import Post_info_form, Upload_image_form, SearchForm
from .models import Post,UploadImages
from django.views.generic import ListView, View
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages


class SearchView(View):
    


    def get(self, *args, **kwargs):
        form = SearchForm()
        context = {'form':form}
        return render(self.request,"HomePage.html",context)

    def post(self, *args, **kwargs):
        # Must get data with forms.ChoiceField() , create choise dictionary, but .... it's too long  
        Class = self.request.POST.get('Class')
        matiere = self.request.POST.get('matiere')
        nature = self.request.POST.get('cour_td')
        Search_info=[]
        Search_info.extend([matiere, Class, nature])
        # print(Search_info)
        
        return redirect("isima_trivez:list_of_post",Search_info)


#TODO:Post the posts that match with value searched 
class PostsView(ListView):
    template_name = 'PostPage.html'
    model = Post

    def get(self, Search_info, *args, **kwargs):
        data = self.request.POST.get('Search_info') #Error TypeError: 'NoneType' object is not subscriptable
        print(data)
        print(type(data))
        try:
            data = self.model.objects.filter(matire=data[0])
            context ={
                'data':data
            }
            return render(self.request, 'PostPage.html', context)
        except ObjectDoesNotExist:
            messages.warning(self.request,"No Items")
            return redirect("/")








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











