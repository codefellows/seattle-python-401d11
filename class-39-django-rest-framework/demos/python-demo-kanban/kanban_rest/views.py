from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .serializers import (
    UserSerializer,
    User,
    CategorySerializer,
    Category,
    CardSerializer,
    Card,
)


class RegisterApiView(generics.CreateAPIView):
    permission_classes = ''
    authentication_classes = (TokenAuthentication,)
    serializer_class = UserSerializer


class UserApiView(generics.RetrieveAPIView):
    permission_classes = ''
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(id=self.kwargs['pk'])


class CategoryListApiView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(
            user__username=self.request.user.username)

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)


class CategoryDetailApiView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(
            user__username=self.request.user.username)


class CardListApiView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = CardSerializer

    def get_queryset(self):
        return Card.objects.filter(
            category__user__username=self.request.user.username)


class CardDetailApiView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = CardSerializer

    def get_queryset(self):
        return Card.objects.filter(
            category__user__username=self.request.user.username)
