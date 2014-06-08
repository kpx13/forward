# -*- coding: utf-8 -*-
from django.contrib import admin
import models

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('slug', 'title', 'desc', 'sort_parameter')
    search_fields = ('title', 'content')

admin.site.register(models.Service, ArticleAdmin)