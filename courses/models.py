from django.db import models
from django.utils.safestring import mark_safe
from mptt.models import MPTTModel
from django.contrib.auth.models import User


class Courses(models.Model):
    title = models.CharField('Sarlavhasi', max_length=300)
    slug = models.SlugField(max_length=200, unique=True)
    price = models.CharField('narxi', max_length=100)
    sub_description = models.TextField('Qisqa malumot', max_length=300)
    description1 = models.TextField('Malumot 1', max_length=1000)
    description2 = models.TextField('Malumot 2', max_length=1000, blank=True)
    description3 = models.TextField('Malumot 3', max_length=1000, blank=True)
    instructor = models.CharField('O`qituvchi', max_length=200)
    duration = models.CharField('Davomiyligi', max_length=200)
    language = models.CharField('Kurs tili', max_length=200)
    image = models.ImageField('Rasmi', upload_to='images/')

    class Meta:
        verbose_name = "Kurslar"
        verbose_name_plural = "Kurslar"

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50">'.format(self.image.url))

    image_tag.short_description = 'Image'


class FeaturedCourse(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name="Course")

    class Meta:
        verbose_name = 'Featured Course'
        verbose_name_plural = 'Featured Course'
