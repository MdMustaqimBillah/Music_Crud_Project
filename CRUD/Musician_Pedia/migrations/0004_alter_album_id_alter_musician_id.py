# Generated by Django 5.0.3 on 2024-03-25 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Musician_Pedia', '0003_rename_ratings_album_album_ratings_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='musician',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
