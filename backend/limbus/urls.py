from django.urls import path
from . import views

# app_name allows for easier calling of url in html
app_name = "limbus"
# these are the url patterns for each page of the website
urlpatterns = [
    path("skill", views.SkillSerial.as_view(), name="skillView"),
    path("skill_ego", views.SkillEgoSerial.as_view(), name="skill_egoView"),
    path("passive", views.PassiveSerial.as_view(), name="passiveView"),
    path("passive_ego", views.PassiveEgoSerial.as_view(), name="passive_egoView"),
    path("identity", views.IdentitySerial.as_view(), name="identityView"),
    path("EGO", views.EGOSerial.as_view(), name="EGOView"),
    path(
        "battle_keyword", views.BattleKeywordSerial.as_view(), name="battle_keywordView"
    ),
]
