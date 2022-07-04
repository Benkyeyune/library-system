from django.shortcuts import render
from django.http import HttpResponse
from .models import Books

app_name = 'books'


def index(request):

    all_books = Books.objects.all()
    return render(request, 'index.html', {'books': all_books})
