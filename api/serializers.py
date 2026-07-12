from rest_framework import serializers
from .models import Card, Deck

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ["deck_id", "index", "front", "back", "score"]

class DeckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deck
        fields = ["id", "name"]
