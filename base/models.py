from asyncio.windows_events import NULL
from operator import truth
from tkinter import CASCADE
from turtle import title
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.
class User(AbstractUser):
    is_admin=models.BooleanField(default=False)
    is_librarian=models.BooleanField(default=False)
    is_student=models.BooleanField(default=False)

    class Meta:
        swappable='AUTH_USER_MODEL'




#adding a table for books in the database
class My_book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    ISBN= models.CharField(null=True, blank= True,max_length=200)
    Author= models.CharField(max_length=200)
    Date_added=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)
    book_cover=models.ImageField(upload_to='base/files/covers/',null=True,blank=True)
    added_by=models.CharField(max_length=100,null=True,blank=True)
    subject=models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.title

    def delete(self,*args,**kwargs):
        self.book_cover.delete()
        super().delete(*args,**kwargs)
             

#Adding a table for students in the database
class Student(models.Model):
    name =models.CharField(max_length=200)
    Student_no = models.CharField(max_length=200)
    Reg_no = models.CharField(max_length=200)

#Table for the librarian
class Librarian(models.Model):
    name =models.CharField(max_length=200)
    Staff_Id_no = models.CharField(max_length=200)

class Borrowed_book(models.Model):
    book = models.ForeignKey(My_book,on_delete=models.CASCADE)
    date_borrowed=models.DateTimeField(auto_now_add=True)
    return_date=models.DateTimeField(date_borrowed)
    date_returned=models.DateTimeField()
class Requested_book(models.Model):
    book= models.ForeignKey(My_book,on_delete=models.CASCADE)
    taken=models.BooleanField(default=False)
    




    

