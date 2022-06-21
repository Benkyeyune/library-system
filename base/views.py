from django.shortcuts import render


# Create your views here.
def Home(request):
    return render(request,'base/home.html')

def My_books(request):
    return render(request,'base/My_books.html') 

def sign_up(request):
    return render(request,'base/sign_up.html')
 
