from django.urls import path
from .views import (
    upload_post,
    HomeView,
)

app_name = 'isima_trivez'

urlpatterns = [
    path('',HomeView.as_view() ,name='homepage'),
    path('new',upload_post ,name='new_post')
]