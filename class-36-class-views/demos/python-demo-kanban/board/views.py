from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from .models import Category, Card


class CategoryView(LoginRequiredMixin, ListView):
    template_name = 'board/category_list.html'
    context_object_name = 'categories'
    login_url = reverse_lazy('login')

    def get_queryset(self):
        return Category.objects.filter(user__username=self.request.user.username)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cards'] = Card.objects.filter(category__user__username=self.request.user.username)
        return context


class CardView(LoginRequiredMixin, DetailView):
    template_name = 'board/card_detail.html'
    model = Card
    context_object_name = 'card'
    login_url = reverse_lazy('login')
    pk_url_kwarg = 'id'

    def get_queryset(self):
        return Card.objects.filter(category__user__username=self.request.user.username)
