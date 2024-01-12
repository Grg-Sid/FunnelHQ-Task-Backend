# Generated by Django 5.0.1 on 2024-01-12 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_books_author_alter_books_genre_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='genre',
        ),
        migrations.AddField(
            model_name='books',
            name='gnere',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='genre',
            field=models.TextField(max_length=500),
        ),
    ]
