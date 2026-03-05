from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def home(request):

    return JsonResponse({
        "sistema": "Pizzalab",
        "versao": "1.0",
        "status": "online",
        "descricao": "Sistema web para gestão de pedidos, clientes, produção e cardápio",
        "rotas disponiveis": {
            "admin":"/admin/",
            "cardapio": "/cardapio/",
            "clientes": "/clientes",
            "pedidos": "/pedidos/",
            "producao": "/producao/",
        }
    })