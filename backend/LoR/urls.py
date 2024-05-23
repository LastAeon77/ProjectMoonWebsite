from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# app_name allows for easier calling of url in html
app_name = "lor"
# these are the url patterns for each page of the website
urlpatterns = [
    path("lor/deck/<int:pk>", views.deckSerail.as_view(), name="DeckAPIView"),
    path("lor/deck", views.deckSerailAll.as_view(), name="DeckFullAPIView"),
    path("lor/card/", views.CardListView.as_view(), name="CardAPIView"),
    path("lor/abno/", views.AbnoViewSet.as_view(), name="AbnoAPIView"),
    path("lor/abno/<int:pk>", views.AbnoViewOne.as_view(), name="AbnoAPISingle"),
    path("lor/rank", views.rankSerial.as_view(), name="Rank"),
    path("lor/effects", views.EffectListView.as_view(), name="Effects"),
    path("lor/cardid", views.CardNameID.as_view(), name="CardIDList"),
    path("lor/officeid", views.OfficeFloor.as_view(), name="OfficeIDList"),
    path("lor/pageid", views.PageID.as_view(), name="PageIDList"),
    path("lor/card/<slug:slug>", views.CardView.as_view(), name="SingleCardView"),
    path("lor/cardlight", views.CardLightListView.as_view(), name="CardLightView"),
    path("lor/cardtest/", views.CardListView2.as_view(), name="CardTestAPI"),
    path("lor/deckcreate/", views.DeckCreate.as_view(), name="DeckCreate"),
    path("lor/office", views.OfficeAll.as_view(), name="AllOffice"),
    path("lor/page", views.PageView.as_view(), name="PageList"),
    path("lor/delete_deck", views.DeckDelete.as_view(), name="DeleteDeck"),
    path("lor/userdecks", views.UserDecks.as_view(), name="UserDecks"),
    path("lor/decklight", views.get_deck_name_list, name="decklight"),

] + staticfiles_urlpatterns()
