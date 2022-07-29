from django.shortcuts import render, redirect
from .models import Book,Borrowed_book
from django.contrib.auth.models import User, auth
from .forms import bookform
from django.http import HttpResponseRedirect
from django.contrib import messages,auth
#import pdf stuff
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

#import paginator stuff
from django.core.paginator import Paginator

app_name='books'

def welcome(request):
    return render(request,'books/welcome_page.html')

'''def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            if user.is_superuser:
                return redirect('Home')

        else:
            messages.info(request, "Invalid username or password")
            return redirect('books:login')
    else:
        return render(request, 'books/login.html')


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
                user.save()
                print('user created')

        else:
            print('password not matching')
            return redirect('books:register')

        return redirect('/')

    else:
        return render(request, 'register.html')'''

#Student views
def my_book(request):
    context={}
    return render(request,'books/My_books.html',context) 

def payments_student(request):
    return render(request,'books/payments_student.html')

def Home_student(request):
    books=Book.objects.all().order_by('?')
    #Setup pagination
    p=Paginator(Book.objects.all(),2)
    page=request.GET.get('page')
    books_list=p.get_page(page)
    context={'books':books,
    'books_list':books_list}
    return render(request,'books/home_student.html',context)

def search_books(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        books=Book.objects.filter(book_title__contains=searched)
        return render(request,'books/search_books.html',
        {'searched':searched,
        'books':books})
    else:
        return render(request,'books/search_books.html')

def book_student(request, pk):
    book=Book.objects.get(id=pk)
    context = {'book': book}      
    return render(request,'books/book_student.html',context)

#Librarian views
def Home(request):
    books=Book.objects.all().order_by('Date_added')
     #Setup pagination
    p=Paginator(Book.objects.all(),2)
    page=request.GET.get('page')
    books_list=p.get_page(page)
    context={'books':books,
    'books_list':books_list}
    return render(request,'books/home.html',context)

def add_book(request):
    submitted=False
    if request.method =="POST":
        form =bookform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('books:Home')
            #return HttpResponseRedirect('/add_book?submitted=True')
    else:
        form=bookform
        if 'submitted' in request.GET:
            submitted=True
    form=bookform   
    context={'form':form,'submitted':submitted}
    #messages.info(request,("book was added successfully...."))
    return render(request,'books/add_book.html',context)

def borrwed_books(request):
    Books=Borrowed_book.objects.filter()
    context={'Books':Books}
    return render(request,'books/borrowed_books.html',context)

def requested_books(request):
    My_books=Book.objects.all()
    context={'My_books':My_books}
    return render(request,'books/requested_books.html',context)


def book_librarian(request, pk):
    book=Book.objects.get(id=pk)
    context = {'book': book}      
    return render(request,'books/book_librarian.html',context)

def update_book(request,id):
    book=Book.objects.get(pk=id)
    form=bookform(request.POST or None,request.FILES or None,instance=book)
    if form.is_valid():
        form.save()
        #messages.info(request,("Book updated successfully...."))
        return redirect('books:Home')
    return render(request,'books/update_book.html',
    {'book':book,
    'form':form})   

def delete_book(request,id):
    book=Book.objects.get(pk=id)
    book.delete()
    return redirect('books:Home')

def search_books_librarian(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        books=Book.objects.filter(book_title__contains=searched)
        return render(request,'books/search_books_librarian.html',
        {'searched':searched,
        'books':books})
    else:
        return render(request,'books/search_books_librarian.html')  

#generate a pdf file of booklist
def book_report(request):
    #create bytestream buffer
    buf=io.BytesIO()
    #create canvas
    canv=canvas.Canvas(buf,pagesize=letter,bottomup=0)
    #create text object
    textob= canv.beginText()
    textob.setTextOrigin(inch,inch)
    textob.setFont("Helvetica",14)
  
    #designate model
    books=Book.objects.all()
    #blank list
    lines=[]
    for book in books:
        lines.append(book.book_title)
        lines.append(book.description)
        lines.append(book.Author)
        lines.append(book.subject)
        lines.append("")
        
    #loop
    for line in lines:
        textob.textLine(line)

    #finish up
    canv.drawText(textob)
    canv.showPage()
    canv.save()
    buf.seek(0)

    #return response
    return FileResponse(buf,as_attachment=True,filename='report.pdf')    
