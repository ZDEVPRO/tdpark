# Generated by Django 4.0.2 on 2022-02-16 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_featuredcourse'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='featuredcourse',
            options={'verbose_name': 'Featured Course', 'verbose_name_plural': 'Featured Course'},
        ),
    ]