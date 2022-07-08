from multiprocessing import context
from django.shortcuts import redirect, render
from base.models import My_book
from .forms import bookform
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.
def Home(request):
    My_books=My_book.objects.all().order_by('Date_added')
    context={'My_books':My_books}
    return render(request,'base/home.html',context)

def my_book(request):
    context={'My_book':My_book}
    return render(request,'base/My_books.html',context) 

def welcome(request):
    return render(request,'base/welcome_page.html')
 
def payments_student(request):
    return render(request,'base/payments_student.html')


def add_book(request):
    submitted=False
    if request.method =="POST":
        form =bookform(request.POST)
        ''' book=My_book()
        book.book_cover=request.FILES['book_cover']
        book.save()'''
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


def Home_student(request):
    books=My_book.objects.all().order_by('?')
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

def book_list(request):
    book_list=My_book.objects.all()
    return render(request,'base/home.html',{'book_list': book_list})    

def search_books(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        books=My_book.objects.filter(title__contains=searched)
        return render(request,'base/search_books.html',
        {'searched':searched,
        'books':books})
    else:
        return render(request,'base/search_books.html')

 
def book_student(request, pk):
    book=My_book.objects.get(id=pk)
    context = {'book': book}      
    return render(request,'base/book_student.html',context)


def book_librarian(request, pk):
    book=My_book.objects.get(id=pk)
    context = {'book': book}      
    return render(request,'base/book_librarian.html',context)


def update_book(request,id):
    book=My_book.objects.get(pk=id)
    form=bookform(request.POST or None,instance=book)
    if form.is_valid():
        form.save()
        messages.success(request,("Book updated successfully...."))
        return redirect('Home')
    return render(request,'base/update_book.html',
    {'book':book,
    'form':form})    

def delete_book(request,id):
    book=My_book.objects.get(pk=id)
    book.delete()
    return redirect('Home')
 
def search_books_librarian(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        books=My_book.objects.filter(title__contains=searched)
        return render(request,'base/search_books_librarian.html',
        {'searched':searched,
        'books':books})
    else:
        return render(request,'base/search_books_librarian.html')