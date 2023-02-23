from django.contrib import admin
from .models import MainMenu, Item

class ItemInline(admin.TabularInline):
  model = Item
  # prepopulated_fields = {
  #   'slug': ('name', )
  # }

class MainMenuAdmin(admin.ModelAdmin):
    inlines = [
      ItemInline,
    ]

admin.site.register(MainMenu, MainMenuAdmin)