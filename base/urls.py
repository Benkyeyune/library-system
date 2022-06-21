from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name="Home"),
    path('My_books/', views.My_books, name="My_books"),
    path('sign_up/', views.sign_up,name="sign up"),
]
