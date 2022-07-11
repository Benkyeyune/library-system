from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from base.models import User

# Create your views here.
def login_user(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            #Redirect to success page
            return redirect('Home')    

        else:
            #return an 'invalid login' error
            messages.success(request,("There was an error Logging in, Try again...."))
            return redirect('/users/login_user')    

    else:
        return render(request, 'authenticate/login.html',{})

def logout_user(request):
    logout(request)  
    messages.success(request,("You were logged out successfully...."))
    return redirect('/users/login_user')      

def register_user(request):
    if request.method == "POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            messages.success(request,("Account created successfully...."))
            return redirect('/users/login_user') 
    else:
        form=UserCreationForm
    return render(request, 'authenticate/register_user.html',{'form':form})

'''def login_user(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)

        if user is not None and user.is_active:
            login(request,user)
            #Redirect to success page
            if User.is_admin or User.is_superuser:
                return redirect('admin')
            elif User.is_librarian:
                return redirect('Home')
            else:
                return redirect('Home_student') '''