from django.db import models

# Create your models here.
#adding a table for books in the database
class My_books(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    book_id= models.AutoField
    ISBN= models.CharField(null=True, blank= True,max_length=200)
    Author= models.CharField(max_length=200)
    Date_added=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)
    book_cover=models.ImageField(verbose_name="",width_field="",height_field="")
    book_file=models.FileField(upload_to='files/', null=True, verbose_name="")

    def __str__(self):
        return self.name

#Adding a table for students in the database
class Students(models.Model):
    name =models.CharField(max_length=200)
    Id=models.AutoField
    Student_no = models.CharField(max_length=200)
    Reg_no = models.CharField(max_length=200)

#Table for the librarian

class Librarian(models.Model):
    name =models.CharField(max_length=200)
    Id=models.AutoField
    Staff_Id_no = models.CharField(max_length=200)







    

