from django import forms
from django.forms import ModelForm
from .models import My_book


#create an add book form
class bookform(ModelForm):
    class Meta:
        model=My_book
        fields=('title','description','ISBN','Author','book_cover','added_by')