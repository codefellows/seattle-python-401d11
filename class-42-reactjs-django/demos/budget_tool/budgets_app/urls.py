from django.urls import path
from .views import BudgetListView, TransactionListView, TransactionDetailView
from .views import BudgetCreateView, TransactionCreateView


urlpatterns = [
    path('', BudgetListView.as_view(), name='budgets'),
    path('<int:pk>', TransactionListView.as_view(), name='transactions'),
    path('add/', BudgetCreateView.as_view(), name='budget_add'),
    path('transactions/<int:pk>', TransactionDetailView.as_view(), name='transaction'),
    path('<int:pk>/add/', TransactionCreateView.as_view(), name='transaction_add')
]
