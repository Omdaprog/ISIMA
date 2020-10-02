from django.shortcuts import render, redirect
from .forms import Post_info_form, Upload_image_form
from .models import Post,UploadImages

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
    return render(request, 'base.html', context)











