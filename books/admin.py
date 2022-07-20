from django.contrib import admin
from .models import Books


class BookAdmin(admin.ModelAdmin):
    list_display = ('book_title','author','edition','publication_date','subject_area')


admin.site.register(Books,BookAdmin)
