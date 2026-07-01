from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FilmesViewSet, GenerosViewSet

router = DefaultRouter()

router.register(r'generos', GenerosViewSet, basename='generos')
router.register(r'', FilmesViewSet, basename='filmes')

urlpatterns = [
    path('', include(router.urls)),
]