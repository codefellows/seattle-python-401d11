from django.contrib import admin
from .models import Budget, Transaction


admin.site.register((Budget, Transaction))
