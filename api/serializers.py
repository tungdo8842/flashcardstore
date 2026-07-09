from rest_framework import serializers
from .models import Card, CardList

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ["card_list", "index", "front", "back", "score"]

class CardListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardList
        fields = ["id", "name"]
