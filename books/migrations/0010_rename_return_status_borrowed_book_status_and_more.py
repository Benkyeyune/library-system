# Generated by Django 4.0.5 on 2022-08-08 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_remove_borrowed_book_fine_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='borrowed_book',
            old_name='return_status',
            new_name='status',
        ),
        migrations.RenameField(
            model_name='issued_book',
            old_name='date_borrowed',
            new_name='date_issued',
        ),
        migrations.RemoveField(
            model_name='issued_book',
            name='pickup_date',
        ),
    ]
