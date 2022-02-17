from django.db import models
from django.utils.safestring import mark_safe
from mptt.models import MPTTModel
from django.contrib.auth.models import User


class Blog(models.Model):
    title = models.TextField('Sarlavhasi', max_length=351)
    slug = models.SlugField(max_length=200, unique=True)
    description1 = models.TextField('Tavsifi', max_length=2000)
    description2 = models.TextField('Hamma Tekst', blank=True, max_length=3001)
    description3 = models.TextField('Pastki Tavsif:', blank=True, max_length=1000)
    image = models.ImageField('Rasmi', upload_to='images/')
    create_on_date = models.DateField(auto_now=True)
    create_on_time = models.TimeField(auto_now=True)

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blog"

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50">'.format(self.image.url))

    image_tag.short_description = 'Image'


class HomeBlog(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="Blog")

    class Meta:
        verbose_name = 'Home Blog'
        verbose_name_plural = 'Home Blog'
