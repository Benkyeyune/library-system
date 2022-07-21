from django.shortcuts import render, redirect
from .models import Books
from django.contrib.auth.models import User, auth
from django.contrib import messages, auth
from django.contrib.auth import authenticate, logout


app_name = 'books'


def index(request):

    all_books = Books.objects.all()
    return render(request, 'index.html', {'books': all_books})


def home(request):
    return render(request, 'home.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            if user.is_superuser:
                return redirect('books:home')
            else:
                return redirect('books:home')
        else:
            messages.info(request, "Invalid username or password")
            return redirect('books:login')
    else:
        return render(request, 'login.html')


def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('books:register')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('books:register')

            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save();
                print('user created')

        else:
            print('password not matching')
            return redirect('books:register')

        return redirect('/')

    else:
        return render(request, 'register.html')


