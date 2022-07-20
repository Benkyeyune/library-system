from multiprocessing import context
from django.shortcuts import redirect, render
from base.models import My_book,Borrowed_book
from .forms import bookform
from django.http import HttpResponseRedirect
from django.contrib import messages
#import pdf stuff
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

#import paginator stuff
from django.core.paginator import Paginator

# Create your views here.
def Home(request):
    books=My_book.objects.all().order_by('Date_added')
     #Setup pagination
    p=Paginator(My_book.objects.all(),2)
    page=request.GET.get('page')
    books_list=p.get_page(page)
    context={'books':books,
    'books_list':books_list}
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
        form =bookform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Home')
            #return HttpResponseRedirect('/add_book?submitted=True')
    else:
        form=bookform
        if 'submitted' in request.GET:
            submitted=True
    form=bookform   
    context={'form':form,'submitted':submitted}
    return render(request,'base/add_book.html',context)


def Home_student(request):
    books=My_book.objects.all().order_by('?')
    #Setup pagination
    p=Paginator(My_book.objects.all(),2)
    page=request.GET.get('page')
    books_list=p.get_page(page)
    context={'books':books,
    'books_list':books_list}
    return render(request,'base/home_student.html',context)

def borrwed_books(request):
    Books=Borrowed_book.objects.filter()
    context={'Books':Books}
    return render(request,'base/borrowed_books.html',context)

def requested_books(request):
    My_books=My_book.objects.all()
    context={'My_books':My_books}
    return render(request,'base/requested_books.html',context)

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
    form=bookform(request.POST or None,request.FILES or None,instance=book)
    if form.is_valid():
        form.save()
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
    books=My_book.objects.all()
    #blank list
    lines=['Books added to the Library']
    for book in books:
        lines.append(book.title)
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

