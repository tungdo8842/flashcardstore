from django.urls import path
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns = [
    path("decks/", views.DeckCreation.as_view(), name="deck-view-create"),
    path("decks/<int:pk>/", views.DeckRetrieveUpdateDestroy.as_view(), name="deck-retrieve-update-destroy"),
    path("cards/", views.CardCreation.as_view(), name="card-view-create"),
    path("cards/<int:deck_id>/", views.CardsFromDeck.as_view(), name="card-view-from-deck"),
    path("cards/<int:deck_id>/<int:index>/", views.CardRetrieveUpdateDestroy.as_view(), name="card-retrieve-update-destroy"),

    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
    path('register/', views.RegisterView.as_view(), name="register"),
]
