from django.urls import path
from . import views

urlpatterns = [
    path("cardlists/", views.CardListCreation.as_view(), name="card-list-view-create"),
    path("cardlists/<int:pk>/", views.CardListRetrieveUpdateDestroy.as_view(), name="card-list-retrieve-update-destroy"),
    path("cards/", views.CardCreation.as_view(), name="card-view-create"),
    path("cards/<int:card_list>/", views.CardsFromList.as_view(), name="card-view-from-list"),
    path("cards/<int:card_list>/<int:index>/", views.CardRetrieveUpdateDestroy.as_view(), name="card-retrieve-update-destroy"),
]
