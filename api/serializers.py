from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import Card, Deck

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True) # never return as read

    def validate(self, data):
        user = authenticate(
            username = data["username"], 
            password=data["password"]
        )
        if not user:
            raise serializers.ValidationError("Invalid credentials")
        data["user"] = user
        return data


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ["deck_id", "index", "front", "back", "score"]


class DeckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deck
        fields = ["id", "name"]
