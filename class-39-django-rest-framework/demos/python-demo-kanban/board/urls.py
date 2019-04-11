from django.urls import path
from .views import (
    CategoryView,
    CardView,
    CategoryCreateView,
    CardCreateView,
)

urlpatterns = [
    path('category', CategoryView.as_view(), name='category_view'),
    path('card/<int:id>', CardView.as_view(), name='card_detail'),
    path('category/add', CategoryCreateView.as_view(), name='category_add'),
    path('card/add', CardCreateView.as_view(), name='card_add'),
]
