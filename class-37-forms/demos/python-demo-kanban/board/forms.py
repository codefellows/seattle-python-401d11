from django.forms import ModelForm
from .models import Category, Card


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']


class CardForm(ModelForm):
    class Meta:
        model = Card
        fields = ['assigned_to', 'category', 'title', 'description', 'status']
