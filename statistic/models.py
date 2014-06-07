# -*- coding: utf-8 -*-
from django.db import models

class Stat(models.Model):
    parametr = models.CharField(u'Цифра', max_length=51)
    note = models.CharField(u'Надпись', max_length=127)
    sort_parameter = models.IntegerField(default=0, blank=True, verbose_name=u'порядковый номер')
    
    class Meta:
        verbose_name = 'значение'
        verbose_name_plural = 'статистика на главной'
        ordering = ['sort_parameter']
        
    
    def __unicode__(self):
        return self.note