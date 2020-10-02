from django.urls import path
from .views import upload_post

app_name = 'isima_trivez'

urlpatterns = [
    path('',upload_post ,name='homepage')
]