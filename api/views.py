from rest_framework import generics, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Card, Deck
from .serializers import CardSerializer, DeckSerializer, LoginSerializer


class LoginView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]

        token, _ = Token.objects.get_or_create(user=user) # "created" not osed so _

        return Response({
            'token': token.key,
            'user_id': user.id,
            'username': user.username,
        })


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=204)



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
