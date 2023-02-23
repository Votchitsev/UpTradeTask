from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Item
from .urlHandler import urlHandler


def index(request):
    items = Item.objects.filter(parent=None).all()
    template = loader.get_template('menu/index.html')

    context = {
      'items': items,
    }

    return HttpResponse(template.render(context, request))


def getItems(request, slug):
    queryset = Item.objects.all()

    data = urlHandler(slug, queryset)

    template = loader.get_template('menu/index.html')
    
    context = {
      'items': data
    }

    return HttpResponse(template.render(context, request))
