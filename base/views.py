from django.shortcuts import render


# Create your views here.
def Home(request):
    return render(request,'home.html')

def My_books(request):
    return render(request,'My_books.html')  