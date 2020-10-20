from .forms import Post_info_form, Upload_image_form, SearchForm
from zipfile import ZipFile
from .models import Post,UploadImages
from os.path import basename
from django.http import HttpResponse
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, View
from django.core.exceptions import ObjectDoesNotExist, ImproperlyConfigured
from django.db.models.query import QuerySet


class SearchView(View):
    
    def get(self, *args, **kwargs):
        form = SearchForm()
        context = {'form':form}
        return render(self.request,"HomePage.html",context)

    def post(self, *args, **kwargs):
        # Must get data with forms.ChoiceField() , create choise dictionary, but .... it's too long  
        Class = self.request.POST.get('Class')
        matiere = self.request.POST.get('matiere')
        nature = self.request.POST.get('nature')
               
        return redirect("isima_trivez:list_of_post",Class,matiere,nature)



class PostsView(ListView):
    template_name = 'PostPage.html'
    model = Post
    queryset = None
    
    def get_ordering(self):
    #Return the field or fields to use for ordering the queryset.
        return self.ordering

    def get_queryset(self,*args):

        matiere = self.kwargs['matiere'] 
        Class = self.kwargs['Class']       
        nature = self.kwargs['nature'] 
        print('============================================')       
        print(Class)
        print(not args)
        if (not args )== True :
            if self.queryset is not None:
                queryset = self.queryset
                if isinstance(queryset,QuerySet):
                    queryset = queryset.all()

            elif self.model is not None and matiere == "Matiére" and Class == "Votre Classe" and nature == "Cours ou TD":
                queryset = self.model.objects.all()

            elif self.model is not None and matiere != "Matiére" :
                queryset = self.model.objects.filter(matire=matiere)

            elif self.model is not None and matiere != "Matiére" and Class != "Votre Classe"  :
                queryset = self.model.objects.filter(matire=matiere , degree=Class)

            elif self.model is not None and matiere != "Matiére" and Class != "Votre Classe" and nature != "Cours ou TD" :
                queryset = self.model.objects.filter(matire=matiere ,degree=Class, nature=nature )

            else :
                raise ImproperlyConfigured(
                "%(cls)s is missing a QuerySet. Define "
                "%(cls)s.model, %(cls)s.queryset, or override "
                "%(cls)s.get_queryset()." % {
                    'cls': self.__class__.__name__
                })
        if (not args) == False:
            if self.model is not None and args[0] == "Matiére" and args[1] == "Votre Classe" and args[2] == "Cours ou TD":
                queryset = self.model.objects.all()

            elif self.model is not None and args[0] != "Matiére" :
                queryset = self.model.objects.filter(matire=matiere)

            elif self.model is not None and args[0] != "Matiére" and args[1] != "Votre Classe"  :
                queryset = self.model.objects.filter(matire=matiere , degree=Class)

            elif self.model is not None and args[0] != "Matiére" and args[1] != "Votre Classe" and args[2] != "Cours ou TD" :
                queryset = self.model.objects.filter(matire=matiere ,degree=Class, nature=nature )
        
        ordering = self.get_ordering()
        if ordering : 
            if isinstance(ordering, str):
                ordering = (ordering,)
            queryset = queryset.order_by(*ordering)
        return queryset

    def post(self, request, *args, **kwargs):
        Class = self.request.POST.get('Class')
        matiere = self.request.POST.get('matiere')
        nature = self.request.POST.get('nature')
        object_list = self.get_queryset(Class, matiere, nature)

        return render(request, self.template_name, {'object_list':object_list})

    


   



def upload_post(request):
    
    if request.method == 'POST':
        post_info = Post_info_form(request.POST)
        
        images_uploded = Upload_image_form(request.POST or None, request.FILES or None)
        image = request.FILES.getlist('image')
        

        if post_info.is_valid() and images_uploded.is_valid():
            post = post_info.save(commit=False)
            post.save()
            for f in image:
                
                photos = UploadImages(post=post, image = f)
                
                photos.save()
    else:
        post_info = Post_info_form()
        images_uploded = Upload_image_form()
    context = {
        'post_info': post_info,
        'images_uploded': images_uploded
    }
    return render(request, 'PostDetail.html', context)



def download_zip_file(self, pk):
    """Download archive zip file of code snippets"""
    queryset = get_object_or_404(Post, pk=pk)
    image_list = queryset.uploadimages_set.all()
    response = HttpResponse(content_type='application/zip')
    zf = ZipFile(response, 'w')
    ZIPFILE_NAME = "test.zip"
    for image in image_list:
        url = image.image.url
        url = f"{settings.MEDIA_ROOT}{url[6:]}"
        zf.write(url, basename(url))

    response['Content-Disposition'] = f'attachment; filename={ZIPFILE_NAME}'
    return response







