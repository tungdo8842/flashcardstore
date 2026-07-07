from django.shortcuts import render
from rest_framework import generics
from .models import Card, CardList
from .serializers import CardSerializer, CardListSerializer

# Create your views here.
class CardListCreate(generics.ListCreateAPIView):
    queryset = CardList.objects.all()
    serializer_class = CardListSerializer
