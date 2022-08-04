from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


class Book(models.Model):
    book_title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    edition = models.CharField(max_length=255)
    Date_added = models.DateField(auto_now_add=True)
    subject_area = models.CharField(max_length=255)
    book_cover = models.ImageField(upload_to = 'images/')
    added_by=models.CharField(max_length=100,null=True,blank=True)
    date_updated=models.DateTimeField(auto_now=True)
    ISBN= models.CharField(null=True, blank= True,max_length=200)
    description = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.book_title

    def delete(self,*args,**kwargs):
        self.book_cover.delete()
        super().delete(*args,**kwargs)    


class Borrowed_book(models.Model):
    user=models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    date_borrowed=models.DateTimeField(auto_now_add=True)
    return_date=models.DateTimeField(date_borrowed)
    date_returned=models.DateTimeField()        