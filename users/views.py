from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from books.models import User

# Create your views here.


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            #Redirect to success page
            return redirect('books:Home')    

        else:
            #return an 'invalid login' error
            messages.info(request,("There was an error Logging in, Try again...."))
            return redirect('/users/login_user')    

    else:
        return render(request, 'authenticate/login.html',{})


def logout_user(request):
    logout(request)  
    messages.success(request,("You have logged out successfully...."))
    return redirect('books:welcome')


def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            messages.success(request,("Account created successfully...."))
            return redirect('books:welcome') 
    else:
        form = UserCreationForm
    return render(request, 'authenticate/register_user.html',{'form':form})
