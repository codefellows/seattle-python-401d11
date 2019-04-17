from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from .serializers import (
    UserSerializer, User,
    BudgetSerializer, Budget,
    TransactionSerializer, Transaction
)


class UserAPIView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = ''

    def get_queryset(self):
        return User.objects.filter(id=self.kwargs['pk'])


class RegisterAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = ''
    authentication_classes = (TokenAuthentication, )


class BudgetListAPIView(generics.ListCreateAPIView):
    serializer_class = BudgetSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        return Budget.objects.filter(
            user__username=self.request.user.username)

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)


class BudgetDetailAPIView(generics.RetrieveAPIView):
    serializer_class = BudgetSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        return Budget.objects.filter(
            user__username=self.request.user.username)


class TransactionListAPIView(generics.ListCreateAPIView):
    serializer_class = TransactionSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        return Transaction.objects.filter(
            budget__user__username=self.request.user.username)

    def perform_create(self, serializer):
        budget = Budget.objects.get(name=self.request.data['budget_name'])
        serializer.save(budget_id=budget.id)


class TransactionDetailAPIView(generics.RetrieveAPIView):
    serializer_class = TransactionSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        return Transaction.objects.filter(
            budget__user__username=self.request.user.username)
