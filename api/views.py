from rest_framework import generics, status
# from rest_framework.response import Response
from .models import Card, CardList
from .serializers import CardSerializer, CardListSerializer

# Create your views here.
class CardListCreation(generics.ListCreateAPIView):
    queryset = CardList.objects.all()
    serializer_class = CardListSerializer

    # def delete(self, request, *args, **kwargs):
    #     CardList.objects.all().delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


class CardListRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = CardList.objects.all()
    serializer_class = CardListSerializer
    lookup_field = "pk"


class CardCreation(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class CardsFromList(generics.ListAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    lookup_field = ""


class CardRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def get_object(self):
        queryset = self.queryset
        obj = generics.get_object_or_404(
            queryset,
            card_list=self.kwargs["card_list"],
            index=self.kwargs["index"]
        )
        self.check_object_permissions(self.request, obj)
        return obj
