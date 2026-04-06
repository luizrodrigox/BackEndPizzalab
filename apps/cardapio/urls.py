from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar),
    path('criar/', views.criar),
    path('<int:id>/', views.detalhe),
    path('atualizar/<int:id>/', views.atualizar),
    path('deletar/<int:id>/', views.deletar),
]
