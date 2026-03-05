from django.urls import path
from .views import listaPedidos, detalhePedido

urlpatterns = [
    path('', listaPedidos),
    path('<int:id>/', detalhePedido),
]
