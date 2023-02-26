from django import template

from ..models import Item
from ..urlHandler import urlHandler


register = template.Library()


@register.inclusion_tag('draw_menu.html', takes_context=True)
def draw_menu(context, menu_name):
    items = Item.objects.filter(menu__name=menu_name)

    data = urlHandler(context['slug'], items)

    return {
        "title": menu_name,
        "items": data,
        }
