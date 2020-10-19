from django.urls import path
from .views import (
    upload_post,
    SearchView,
    PostsView,
    download_zip_file,
)

app_name = 'isima_trivez'

urlpatterns = [
    path('',SearchView.as_view() ,name='homepage'),
    path('posts/<Class>,<matiere>,<nature>',PostsView.as_view(),name='list_of_post'), 
    path('new',upload_post ,name='new_post'),
    path('download/<int:pk>',download_zip_file ,name='download')
]