# Generated by Django 4.0.2 on 2022-02-16 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_remove_footermeta_image_footermeta_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aloqa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('email', models.CharField(blank=True, max_length=100)),
                ('phone', models.CharField(max_length=50)),
                ('message', models.TextField(max_length=1000)),
                ('create_date', models.DateField(auto_now=True)),
                ('create_time', models.TimeField(auto_now=True)),
                ('ip', models.CharField(blank=True, max_length=50)),
            ],
            options={
                'verbose_name': 'Aloqa Formasi',
                'verbose_name_plural': 'Aloqa Formasi',
            },
        ),
    ]
