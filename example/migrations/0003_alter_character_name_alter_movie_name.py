# Generated by Django 5.0.6 on 2024-06-14 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0002_movie_character'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='movie',
            name='name',
            field=models.CharField(max_length=15),
        ),
    ]