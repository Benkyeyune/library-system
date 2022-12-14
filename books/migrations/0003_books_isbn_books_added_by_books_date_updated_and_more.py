# Generated by Django 4.0.5 on 2022-07-29 07:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0002_books_publication_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='ISBN',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='books',
            name='added_by',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='books',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='books',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='image_url',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='books',
            name='publication_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.CreateModel(
            name='Borrowed_book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_borrowed', models.DateTimeField(auto_now_add=True)),
                ('return_date', models.DateTimeField(verbose_name=models.DateTimeField(auto_now_add=True))),
                ('date_returned', models.DateTimeField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.books')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
