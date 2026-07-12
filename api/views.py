from rest_framework import generics, status
# from rest_framework.response import Response
from .models import Card, Deck
from .serializers import CardSerializer, DeckSerializer

# Create your views here.
class DeckCreation(generics.ListCreateAPIView):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer

    # def delete(self, request, *args, **kwargs):
    #     Deck.objects.all().delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


class DeckRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer
    lookup_field = "pk"


class CardCreation(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class CardsFromDeck(generics.ListAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def get_queryset(self):
        return Card.objects.filter(deck_id = self.kwargs["deck_id"])


class CardRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def get_object(self):
        queryset = self.queryset
        obj = generics.get_object_or_404(
            queryset,
            deck_id=self.kwargs["deck_id"],
            index=self.kwargs["index"]
        )
        self.check_object_permissions(self.request, obj)
        return obj
