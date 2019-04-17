from django.urls import path
from .views import (
    UserAPIView, RegisterAPIView,
    BudgetListAPIView, BudgetDetailAPIView,
    TransactionListAPIView, TransactionDetailAPIView)
from rest_framework.authtoken import views


urlpatterns = [
    path('user/<int:pk>',
         UserAPIView.as_view(), name='user_api'),
    path('register',
         RegisterAPIView.as_view(), name='register_api'),
    path('login',
         views.obtain_auth_token, name='login_api'),
    path('budgets/',
         BudgetListAPIView.as_view(), name='budget_list_api'),
    path('budgets/<int:pk>',
         BudgetDetailAPIView.as_view(), name='budget_detail_api'),
    path('transactions/',
         TransactionListAPIView.as_view(), name='transaction_list_api'),
    path('transactions/<int:pk>',
         TransactionDetailAPIView.as_view(), name='transaction_list_api')
]
