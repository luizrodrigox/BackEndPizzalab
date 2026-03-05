from django.urls import path
from .views import listaCardapio, detalhePizza

urlpatterns = [
    path('', listaCardapio),
    path('<int:id>/', detalhePizza),
]
