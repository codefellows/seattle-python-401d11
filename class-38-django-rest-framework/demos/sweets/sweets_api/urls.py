from django.urls import path
from .views import SweetListAPIView

urlpatterns = [
    path('sweets/', SweetListAPIView.as_view(), name='sweet_list_api')
]
