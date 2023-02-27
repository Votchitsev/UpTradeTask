from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('index.html')

    context = {
      'slug': None
    }

    return HttpResponse(template.render(context, request))


def getItems(request, slug):
    template = loader.get_template('index.html')
    
    context = {
      'slug': slug,
    }

    return HttpResponse(template.render(context, request))
