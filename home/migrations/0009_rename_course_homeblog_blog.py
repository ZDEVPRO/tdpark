# Generated by Django 4.0.2 on 2022-02-16 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_homeblog'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homeblog',
            old_name='course',
            new_name='blog',
        ),
    ]
