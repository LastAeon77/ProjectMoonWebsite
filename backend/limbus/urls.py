from django.urls import path
from . import views

# app_name allows for easier calling of url in html
app_name = "limbus"
# these are the url patterns for each page of the website
urlpatterns = [
    path("identity", views.IdentitySerial.as_view(), name="identityView"),
    path("EGO", views.EGOSerial.as_view(), name="EGOView"),
]
