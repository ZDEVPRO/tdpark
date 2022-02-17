# Generated by Django 4.0.2 on 2022-02-16 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_courses_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeaturedCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Course', to='courses.courses')),
            ],
        ),
    ]
