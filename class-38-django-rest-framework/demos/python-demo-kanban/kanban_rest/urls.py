from .views import RegisterApiView, UserApiView
from django.urls import path
from rest_framework.authtoken import views


urlpatterns = [
    path('user/<int:pk>', UserApiView.as_view(), name='user-detail'),
    path('register', RegisterApiView.as_view(), name='register'),
    path('login', views.obtain_auth_token),
]
