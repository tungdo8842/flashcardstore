from django.urls import path
from . import views

urlpatterns = [
    path("cards/", views.CardListCreate.as_view(), name="card-view-create"),
]
