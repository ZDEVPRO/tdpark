# Generated by Django 4.0.2 on 2022-02-16 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_aboutsection'),
    ]

    operations = [
        migrations.CreateModel(
            name='Total',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num1', models.CharField(max_length=100)),
                ('num2', models.CharField(max_length=100)),
                ('num3', models.CharField(max_length=100)),
                ('num4', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Hisob',
                'verbose_name_plural': 'Hisob',
            },
        ),
    ]
