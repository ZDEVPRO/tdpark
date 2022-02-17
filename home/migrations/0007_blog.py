# Generated by Django 4.0.2 on 2022-02-16 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=351, verbose_name='Sarlavhasi')),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('description1', models.TextField(max_length=2000, verbose_name='Tavsifi')),
                ('description2', models.TextField(blank=True, max_length=3001, verbose_name='Hamma Tekst')),
                ('description3', models.TextField(blank=True, max_length=1000, verbose_name='Pastki Tavsif:')),
                ('image', models.ImageField(upload_to='images/', verbose_name='Rasmi')),
                ('create_on_date', models.DateField(auto_now=True)),
                ('create_on_time', models.TimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blog',
            },
        ),
    ]