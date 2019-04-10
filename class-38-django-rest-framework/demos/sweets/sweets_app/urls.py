from django.urls import path
from .views import SweetListView

urlpatterns = [
    path('', SweetListView.as_view(), name='sweet_list')
]
