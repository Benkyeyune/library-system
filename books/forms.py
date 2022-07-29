from django import forms
from django.forms import ModelForm
from .models import Book


#create an add book form
class bookform(ModelForm):
    class Meta:
        model=Book
        fields=('book_title','description','ISBN','author','book_cover','added_by','subject_area')



