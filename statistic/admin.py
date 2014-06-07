# -*- coding: utf-8 -*-
from django.contrib import admin
import models

class StatAdmin(admin.ModelAdmin):
    list_display = ('parametr', 'note', 'sort_parameter')
    ordering = ('sort_parameter', )
    
admin.site.register(models.Stat, StatAdmin)