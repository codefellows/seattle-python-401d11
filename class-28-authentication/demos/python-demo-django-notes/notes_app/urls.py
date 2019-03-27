from .views import note_detail_view, note_list_view
from django.urls import path

urlpatterns = [
    path('<int:pk>', note_detail_view, name='note_detail'),
    path('', note_list_view, name='note_list'),
]
