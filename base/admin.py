from django.contrib import admin

# Register your models here.
from .models import Borrowed_book, My_book, Requested_book,Student,Librarian

#admin.site.register(My_book)
admin.site.register(Student)
admin.site.register(Librarian)
admin.site.register(Requested_book)
admin.site.register(Borrowed_book)
@admin.register(My_book)
class MybookAdmin(admin.ModelAdmin):
    list_display=('title',)
    ordering=('title',)
    search_fields=('title','id')