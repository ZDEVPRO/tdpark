from django.db import models
from django.utils.safestring import mark_safe
from mptt.models import MPTTModel
from django.contrib.auth.models import User


class HeaderLogo(models.Model):
    image = models.ImageField('Rasmi', upload_to='images/')

    class Meta:
        verbose_name = 'Header Logo'
        verbose_name_plural = 'Header Logo'

    def image_tag(self):
        return mark_safe('<img src="{}" height="50">'.format(self.image.url))

    image_tag.short_description = 'Image'


class HomeTitle(models.Model):
    sub_title = models.CharField(max_length=300)
    title = models.TextField(max_length=500)

    button1 = models.CharField(max_length=100)
    slug_button1 = models.CharField(max_length=100)

    button2 = models.CharField(max_length=100)
    slug_button2 = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Home Title'
        verbose_name_plural = 'Home Title'

    def __str__(self):
        return self.title


class AboutSection(models.Model):
    title = models.TextField('Sarlavha', max_length=200)
    description = models.TextField('Malumot', max_length=400)
    button = models.CharField(max_length=50)
    slug_button = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'About Section'
        verbose_name_plural = 'About Section'

    def __str__(self):
        return self.title


class Total(models.Model):
    num1 = models.CharField(max_length=100)
    num2 = models.CharField(max_length=100)
    num3 = models.CharField(max_length=100)
    num4 = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Hisob'
        verbose_name_plural = 'Hisob'

    def __str__(self):
        return self.num1


class Teacher(models.Model):
    name = models.CharField('Ism Familya', max_length=200)
    category = models.CharField('Kasb', max_length=300)
    image = models.ImageField('Rasim', upload_to='images/')
    phone = models.CharField('Telefon raqami', max_length=100)
    whatsapp = models.CharField(blank=True, max_length=100)
    telegram = models.CharField(blank=True, max_length=100)

    class Meta:
        verbose_name = "O'qituvchilar"
        verbose_name_plural = "O'qituvchilar"

    def __str__(self):
        return self.name

    def image_tag(self):
        return mark_safe('<img src="{}" height="50">'.format(self.image.url))

    image_tag.short_description = 'Image'


class AloqaModel(models.Model):
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    message = models.TextField(max_length=500)
    create_time = models.TimeField(auto_now=True, null=True)
    create_date = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Aloqa Formasi'
        verbose_name_plural = 'Aloqa Formasi'
