from django.contrib import admin

# Register your models here.
from .models import My_book,Student,Librarian

admin.site.register(My_book)
admin.site.register(Student)
admin.site.register(Librarian)