from django.contrib import admin
from .models import Category, Card


admin.site.register((Category, Card))
