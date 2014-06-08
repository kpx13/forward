# -*- coding: utf-8 -*-

from django.core.context_processors import csrf
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from feedback.forms import FeedbackForm
from order.forms import OrderForm
import config
from livesettings import config_value
from django.conf import settings

from pages.models import Page
from services.models import Service
from statistic.models import Stat

PAGINATION_COUNT = 5

def get_common_context(request):
    c = {}
    c['lang'] = request.LANGUAGE_CODE
    c['request_url'] = request.path
    c['is_debug'] = settings.DEBUG
    c['field_1'] = config_value('MyApp', 'field_1')
    c['field_2'] = config_value('MyApp', 'field_2')
    c['field_3'] = config_value('MyApp', 'field_3')
    c['field_4'] = config_value('MyApp', 'field_4')
    c['phone'] = config_value('MyApp', 'PHONE')
    
    c.update(csrf(request))
    return c

def page(request, page_name):
    c = get_common_context(request)
    p = Page.get(page_name, request.LANGUAGE_CODE)
    
    if p:
        c.update({'p': p})
        return render_to_response('page.html', c, context_instance=RequestContext(request))
    else:
        raise Http404()

def home(request):
    c = get_common_context(request)
    c['request_url'] = 'home'
    c['content'] = Page.get('home', c['lang'])['content']
    c['stat'] = Stat.objects.all()
    c['services'] = Service.objects.all()
    return render_to_response('home.html', c, context_instance=RequestContext(request))

def about(request):
    c = get_common_context(request)
    c['content'] = Page.get('about', c['lang'])['content']
    return render_to_response('about.html', c, context_instance=RequestContext(request))

def services(request):
    c = get_common_context(request)
    c['left'] = Page.get('servicesleft', c['lang'])['content']
    c['right'] = Page.get('servicesright', c['lang'])['content']
    c['services'] = Service.objects.all()
    return render_to_response('services.html', c, context_instance=RequestContext(request))

def service_det(request, page_name):
    c = get_common_context(request)
    p = Service.get(page_name, request.LANGUAGE_CODE)

    if p:
        c.update({'s': p, 'icon': Service.objects.get(slug=page_name).icon1 })
        return render_to_response('sevice_detail.html', c, context_instance=RequestContext(request))
    else:
        raise Http404()

def order(request):
    c = get_common_context(request)
    #c.update({'p': Page.get('order', c['lang'])})
    if request.method == 'GET':
        c.update({'form': OrderForm()})
    elif request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = OrderForm()
            c['feedback_ok'] = True
        c.update({'form': form})
    return render_to_response('order.html', c, context_instance=RequestContext(request))

def contacts(request):
    c = get_common_context(request)
    c.update({'content': Page.get('contacts', c['lang'])['content']})
    if request.method == 'GET':
        c.update({'form': FeedbackForm()})
    elif request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            form = FeedbackForm()
            c['feedback_ok'] = True
        c.update({'form': form})
    return render_to_response('contacts.html', c, context_instance=RequestContext(request))
