# Generated by Django 5.0.3 on 2024-04-07 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Musician_Pedia', '0006_rename_ratings_album_album_ratings_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Album',
            new_name='Book',
        ),
        migrations.RenameModel(
            old_name='Musician',
            new_name='Writer',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='album_ratings',
            new_name='book_ratings',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='album_title',
            new_name='book_title',
        ),
    ]
