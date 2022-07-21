from django.urls import path
from .import views

app_name = 'books'

urlpatterns = [
    path('', views.home, name='home'),
    path('index', views.index, name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
]