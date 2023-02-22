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


def find(queryset, slug):
    result = queryset.filter(parent__slug=slug)

    current_item = queryset.filter(slug=slug).first()

    while True:
        parent_item = current_item.parent
        
        if parent_item == None:
            result = result | queryset.filter(slug=current_item.slug)
            break

        current_items = queryset.filter(parent__slug=parent_item.slug)

        if result == None:
            result = current_items
        else:
            result = result | current_items

        current_item = current_items[0].parent

    return result


def getItems(request, slug):
    items = Item.objects.filter(parent__slug=slug)

    queryset = Item.objects.all()

    q = find(queryset, slug)

    template = loader.get_template('menu/index.html')
    
    context = {
      'items': q
    }

    return HttpResponse(template.render(context, request))