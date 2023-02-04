from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import (
    ObtainTokenPairWithColorView,
    CustomUserCreate,
    LogoutAndBlacklistRefreshTokenForUserView,
    CheckAuth,
)

urlpatterns = [
    path("user/create/", CustomUserCreate.as_view(), name="create_user"),
    path("token/obtain/", ObtainTokenPairWithColorView.as_view(), name="token_create"),
    path("token/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
    path("checkauth", CheckAuth.as_view(), name="checkauth"),
    path(
        "blacklist/",
        LogoutAndBlacklistRefreshTokenForUserView.as_view(),
        name="blacklist",
    ),
]
