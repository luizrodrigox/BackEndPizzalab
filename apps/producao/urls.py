from django.urls import path
from .views import listaProducao, detalheProducao

urlpatterns = [
    path('', listaProducao),
    path('<int:id>/', detalheProducao),
]
