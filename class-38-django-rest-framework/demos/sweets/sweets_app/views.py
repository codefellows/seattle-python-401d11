from django.shortcuts import render
from django.views.generic import ListView
from .models import Sweet

# Create your views here.
class SweetListView(ListView):
    model = Sweet
    context_object_name = 'sweets'
