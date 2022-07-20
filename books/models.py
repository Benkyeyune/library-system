from django.db import models
from datetime import date


class Books(models.Model):
    book_title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    edition = models.CharField(max_length=255)
    publication_date = models.DateField(default=date.today())
    subject_area = models.CharField(max_length=255)
    image_url = models.ImageField(upload_to = 'images/')



    def __str__(self):
        return self.book_title