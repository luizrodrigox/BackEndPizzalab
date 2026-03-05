from django.urls import path
from .views import listaClientes, detalheCliente

urlpatterns = [
    path('', listaClientes),
    path('<int:id>/', detalheCliente),
]
