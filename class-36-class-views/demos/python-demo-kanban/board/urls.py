from django.urls import path
from .views import CategoryView, CardView

urlpatterns = [
    path('category', CategoryView.as_view(), name='category_view'),
    path('card/<int:id>', CardView.as_view(), name='card_detail'),
]
