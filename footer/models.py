from django.db import models


class FooterMeta(models.Model):
    title = models.CharField('Sarlavha', max_length=200)
    description = models.TextField('Malumot', max_length=400)
    instagram = models.CharField(max_length=200, blank=True)
    telegram = models.CharField(max_length=200, blank=True)
    youtube = models.CharField(max_length=200, blank=True)
    facebook = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name = 'Footer Biz haqimizda'
        verbose_name_plural = 'Footer Biz haqimizda'


class FooterContactMeta(models.Model):
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.TextField(max_length=400)

    class Meta:
        verbose_name = 'Footer Aloqa Malumoti'
        verbose_name_plural = 'Footer Aloqa Malumoti'
