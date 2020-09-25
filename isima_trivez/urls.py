from django.urls import path
from .views import homepage

app_name = 'isima_trivez'

urlpatterns = [
    path('',homepage.as_view() ,name='homepage')
]