# Generated by Django 4.0.2 on 2022-02-16 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_total'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Ism Familya')),
                ('category', models.CharField(max_length=300, verbose_name='Kasb')),
                ('image', models.ImageField(upload_to='images/', verbose_name='Rasim')),
                ('phone', models.CharField(max_length=100, verbose_name='Telefon raqami')),
                ('whatsapp', models.CharField(blank=True, max_length=100)),
                ('telegram', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'verbose_name': "O'qituvchilar",
                'verbose_name_plural': "O'qituvchilar",
            },
        ),
    ]
