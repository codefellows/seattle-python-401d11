from django.shortcuts import render
from rest_framework import generics
from sweets_app.models import Sweet

from .serializers import SweetSerializer

class SweetListAPIView(generics.ListAPIView):
    queryset = Sweet.objects.all()
    serializer_class = SweetSerializer
