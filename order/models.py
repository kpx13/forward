# -*- coding: utf-8 -*-

from django.db import models
from pytils import translit

class Order(models.Model):
    name  = models.CharField(u'Наименование компании', max_length=512)
    country  = models.CharField(u'Страна', blank=True, max_length=512)
    city  = models.CharField(u'Город', blank=True, max_length=512)
    desc  = models.CharField(u'Описание товара', blank=True, max_length=2048)
    contact  = models.CharField(u'Контактное лицо', blank=True, max_length=255)
    phone  = models.CharField(u'Телефон', blank=True, max_length=255)
    email  = models.CharField(u'Email', blank=True, max_length=255)
    file = models.FileField(upload_to=lambda instance, filename: 'uploads/orders/' + translit.translify(filename), 
                            null=True, blank=True, max_length=256, verbose_name=u'файл')
    request_date = models.DateTimeField(u'дата добавления', auto_now_add=True)
    
    class Meta:
        verbose_name = u'заказ'
        verbose_name_plural = u'заказы'
        ordering = ['-request_date']
    
    def __unicode__(self):
        return str(self.name)

