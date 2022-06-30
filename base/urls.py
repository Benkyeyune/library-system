from django.urls import path
from . import views

urlpatterns = [
    #Librarian urls
    path('', views.Home, name="Home"),
    path('sign_up/', views.sign_up,name="sign up"),
    path('add_book/',views.add_book,name='add_book'),
    path('borrowed_books/',views.borrwed_books,name='borrowed_books'),
    path('requested_books/',views.requested_books,name='requested_books'), 
   #student urls
    path('Home_student/',views.Home_student,name="Home_student"),
    path('payments_student/',views.payments_student,name='My_payments'),
    path('My_books/', views.my_book, name="My_books"),
]
