from django.urls import path
from .import views

app_name = 'books'

urlpatterns = [
    path('', views.index),
    path('home', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('register', views.register, name='register'),
]