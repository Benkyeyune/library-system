from multiprocessing import context
from django.shortcuts import render
from base.models import My_book
from .forms import bookform
from django.http import HttpResponseRedirect
 

# Create your views here.
def Home(request):
    My_books=My_book.objects.all()
    context={'My_books':My_books}
    return render(request,'base/home.html',context)

def my_book(request):
    context={'My_book':My_book}
    return render(request,'base/My_books.html',context) 

def sign_up(request):
    return render(request,'base/sign_up.html')
 
def payments_student(request):
    return render(request,'base/payments_student.html')


def add_book(request):
    submitted=False
    if request.method =="POST":
        form =bookform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_book?submitted=True')
    else:
        form=bookform
        if 'submitted' in request.GET:
            submitted=True
    form=bookform   
    context={'form':form,'submitted':submitted}
    return render(request,'base/add_book.html',context)
books=[
    {'id':1,'title':'geo'},
    {'id':2,'title':'bio'},
    {'id':3,'title':'hen'},

]

def Home_student(request):
    books=My_book.objects.all()
    context={'books':books}
    return render(request,'base/home_student.html',context)

def borrwed_books(request):
    My_books=My_book.objects.all()
    context={'My_books':My_books}
    return render(request,'base/borrowed_books.html',context)

def requested_books(request):
    My_books=My_book.objects.all()
    context={'My_books':My_books}
    return render(request,'base/requested_books.html',context)

def all_books(request):
    book_list=My_book.objects.all()
    return render(request,'base/home_student.html',{'book_list': book_list})

def search_books(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        books=My_book.objects.filter(title__contains=searched)
        return render(request,'base/search_books.html',
        {'searched':searched,
        'books':books})
    else:
        return render(request,'base/search_books.html')

 
def book(request, pk):
    book=My_book.objects.get(id=pk)
    context = {'book': book}      
    return render(request,'base/book.html',context)
