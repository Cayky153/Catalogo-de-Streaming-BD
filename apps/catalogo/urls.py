from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CatalogoViewSet,PlanosViewSet
from .views import PlanosCreateView

router = DefaultRouter()
router.register(r'', CatalogoViewSet,basename='catalogo')
router.register(r'planos', PlanosViewSet,basename='planos')

urlpatterns = [
    path('planos/', PlanosCreateView.as_view(), name='adicionar-plano'),
]