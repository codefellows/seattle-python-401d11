from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView
from .models import Budget, Transaction
from .forms import BudgetForm, TransactionForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class BudgetListView(LoginRequiredMixin, ListView):
    model = Budget
    template_name = 'budget_list.html'
    context_object_name = 'budgets'
    login_url = reverse_lazy('login')

    def get_queryset(self):
        return Budget.objects.filter(user__username=self.request.user.username)


class TransactionListView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = 'transaction_list.html'
    context_object_name = 'transactions'
    login_url = reverse_lazy('login')

    def get_queryset(self):
        return Transaction.objects.filter(budget__id=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['budget'] = Budget.objects.get(pk=self.kwargs['pk'])
        return context


class TransactionDetailView(LoginRequiredMixin, DetailView):
    model = Transaction


class BudgetCreateView(LoginRequiredMixin, CreateView):
    model = Budget
    template_name = 'budget_create.html'
    form_class = BudgetForm
    success_url = reverse_lazy('budgets')
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TransactionCreateView(LoginRequiredMixin, CreateView):
    model = Transaction
    template_name = 'transaction_create.html'
    form_class = TransactionForm
    success_url = reverse_lazy('')
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        transaction = form.save(commit=False)
        transaction.budget = Budget.objects.get(pk=self.kwargs['pk'])
        transaction.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('transactions', kwargs={'pk': self.kwargs['pk']})
