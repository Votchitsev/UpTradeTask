from django.db import models
from django.urls import reverse

class MainMenu(models.Model):
    name = models.CharField(max_length=50)

class Item(models.Model):
    name = models.CharField(max_length=50)
    menu = models.ForeignKey(MainMenu, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', verbose_name='parent', related_name='child', blank=True, null=True, on_delete=models.CASCADE)
    slug = models.SlugField(unique='name')

    def get_absolute_url(self):
        return reverse('items', kwargs={"slug": self.slug})
