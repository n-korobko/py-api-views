from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cinema.views import (
    GenreAPIView,
    ActorGenericAPIView,
    CinemaHallViewSet,
    MovieViewSet,
)

router = DefaultRouter()
router.register("movies", MovieViewSet)
router.register("cinema_halls", CinemaHallViewSet)

urlpatterns = [
    path("genres/", GenreAPIView.as_view()),
    path("genres/<int:pk>/", GenreAPIView.as_view()),

    path("actors/", ActorGenericAPIView.as_view()),
    path("actors/<int:pk>/", ActorGenericAPIView.as_view()),

    path("", include(router.urls)),
]
