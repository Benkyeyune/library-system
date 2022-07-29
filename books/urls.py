from django.urls import path
from .import views

app_name = 'books'

urlpatterns = [
    path('', views.welcome, name='welcome'),
     #Librarian urls
    path('home/', views.Home, name="Home"),
    path('add_book/',views.add_book,name='add_book'),
    path('borrowed_books/',views.borrwed_books,name='borrowed_books'),
    path('requested_books/',views.requested_books,name='requested_books'),
    path('update_book/<id>',views.update_book,name='update_book'),
    path('delete_event/<id>',views.delete_book,name='delete_book'),
    path('search_books_librarian/', views.search_books_librarian, name="search_books_librarian"),
    path('book_librarian/<str:pk>/', views.book_librarian, name="book_librarian"),
    path('book_report', views.book_report, name="book_report"), 
     #student urls
    path('Home_student/',views.Home_student,name="Home_student"),
    path('payments_student/',views.payments_student,name='My_payments'),
    path('My_books/', views.my_book, name="My_books"),
    path('search_books/', views.search_books, name="search_books"),
    path('book_student/<str:pk>/', views.book_student, name="book_student"),



    #path('index', views.index, name='index'),
]