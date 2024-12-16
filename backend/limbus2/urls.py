from django.urls import path
from . import views

# app_name allows for easier calling of url in html
app_name = "limbus2"
# these are the url patterns for each page of the website
urlpatterns = [
    path("identities_name_en", views.IdentityListLite.as_view(), name="identityListLite"),
    path("identity_data/<int:pk>", views.IdentityGet, name="identity"),
    path("ego_data/<int:pk>", views.EgoGet, name="ego"),
    path("story", views.StoryAcquire.as_view(), name="story_acquire"),
    path("story_query",views.ENStoryByChapterAndNode.as_view(),name="story_query"),
    path("story_theater",views.StoryTheaterGet.as_view(),name="story_theater"),
    path("story_random",views.StoryRandom.as_view(),name="story_random"),
    path("en_chapter_list",views.ENChapterNodeList.as_view(),name="en_chapter_list"),
    path("story_acquire_list",views.StoryAcquireList.as_view(),name="story_acquire_list")

]
