# Generated by Django 4.0.2 on 2022-02-16 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_hometitle_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=200, verbose_name='Sarlavha')),
                ('description', models.TextField(max_length=400, verbose_name='Malumot')),
                ('button', models.CharField(max_length=50)),
                ('slug_button', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'About Section',
                'verbose_name_plural': 'About Section',
            },
        ),
    ]
