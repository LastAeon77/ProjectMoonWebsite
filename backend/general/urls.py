from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


# app_name allows for easier calling of url in html
app_name = "general"
# these are the url patterns for each page of the website
urlpatterns = [
    path("interview/<int:pk>", views.InterviewAPIView.as_view(), name="Interview"),
    path("interview", views.InterviewListAPIView.as_view(), name="InterviewList"),
]
