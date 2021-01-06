from django.contrib import admin
from .models import Recette, Restaurant, Shop

# Register your models here.

admin.site.register(Recette)
admin.site.register(Restaurant)
admin.site.register(Shop)