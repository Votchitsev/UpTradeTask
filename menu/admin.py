from django.contrib import admin
from .models import Menu, Item

class ItemInline(admin.TabularInline):
  model = Item


class MenuAdmin(admin.ModelAdmin):
    inlines = [
      ItemInline,
    ]


admin.site.register(Menu, MenuAdmin)