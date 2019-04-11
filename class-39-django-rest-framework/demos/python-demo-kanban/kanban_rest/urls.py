from django.urls import path
from rest_framework.authtoken import views
from .views import (
    RegisterApiView,
    UserApiView,
    CategoryListApiView,
    CategoryDetailApiView,
    CardListApiView,
    CardDetailApiView,
)


urlpatterns = [
    path('user/<int:pk>', UserApiView.as_view(), name='user-detail'),
    path('register', RegisterApiView.as_view(), name='register'),
    path('login', views.obtain_auth_token),
    path('category/', CategoryListApiView.as_view(), name='category-list-api'),
    path('category/<int:pk>', CategoryDetailApiView.as_view(), name='category-detail-api'),
    path('card/', CardListApiView.as_view(), name='card-list-api'),
    path('card/<int:pk>', CardDetailApiView.as_view(), name='card-detail-api'),
]
