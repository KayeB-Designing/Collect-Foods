from django.contrib import admin
from .models import Food, Recipe, Cookbook

admin.site.register(Food)
admin.site.register(Recipe)
admin.site.register(Cookbook)