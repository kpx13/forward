# -*- coding: utf-8 -*-
from django.db import models
from ckeditor.fields import RichTextField
import pytils

class Service(models.Model):
    title = models.CharField(max_length=128, verbose_name=u'заголовок ру')
    title_en = models.CharField(max_length=200, verbose_name=u'заголовок en')
    title_ch = models.CharField(max_length=200, blank=True, verbose_name=u'заголовок ch')

    desc = models.CharField(max_length=512, verbose_name=u'описание краткое ру')
    desc_en = models.CharField(max_length=512, verbose_name=u'описание краткое en')
    desc_ch = models.CharField(max_length=512, verbose_name=u'описание краткое ch')

    content = RichTextField(blank=True, verbose_name=u'контент ру')
    content_en = RichTextField(blank=True, verbose_name=u'контент en')
    content_ch = RichTextField(blank=True, verbose_name=u'контент ch')


    icon1 = models.ImageField(upload_to=lambda instance, filename: 'uploads/service_icons/' + pytils.translit.translify(filename),
	                            max_length=256, verbose_name=u'иконка обычная')
    icon2 = models.ImageField(upload_to=lambda instance, filename: 'uploads/service_icons/' + pytils.translit.translify(filename),
	                            max_length=256, verbose_name=u'иконка красная')
    slug = models.SlugField(verbose_name=u'слаг', unique=True, blank=True, help_text=u'Заполнять не нужно')
    sort_parameter = models.IntegerField(default=0, blank=True, verbose_name=u'порядковый номер')
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=pytils.translit.slugify(self.title)
        super(Service, self).save(*args, **kwargs)
    
    @staticmethod
    def get_by_slug(page_name):
        try:
            return Service.objects.get(slug=page_name)
        except:
            return None
    
    class Meta:
        verbose_name = u'услуга'
        verbose_name_plural = u'услуги'
        ordering=['sort_parameter']
    
    def __unicode__(self):
        return self.slug

    @staticmethod
    def get(slug, lang):
        try:
            page = Service.objects.get(slug=slug)
            if lang=='en':
                return {'title': page.title_en,
                        'content': page.content_en,
                        'desc': page.desc_en,
                        }
            elif lang=='zh-cn':
                return {'title': page.title_ch,
                        'content': page.content_ch,
                        'desc': page.desc_ch,
                        }
            else :
                return {'title': page.title,
                        'content': page.content,
                        'desc': page.desc,
                        }
        except:
            return None