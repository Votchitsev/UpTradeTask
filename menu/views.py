from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Item

def index(request):
    items = Item.objects.filter(parent=None).all()
    template = loader.get_template('menu/index.html')

    context = {
      'items': items,
    }

    return HttpResponse(template.render(context, request))


def getItems(request, slug):
    items = Item.objects.filter(parent__slug=slug)

    queryset = Item.objects.all()

    template = loader.get_template('menu/index.html')
    
    context = {
      'items': queryset
    }

    return HttpResponse(template.render(context, request))
