from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def home(request):

    return JsonResponse({
        "sistema": "Pizzalab",
        "versao": "3.0",
        "status": "online",
        "descricao": "Sistema web para gestão de pedidos, clientes, produção e cardápio",

        "rotas disponiveis": {

            "auth": {
                "register": "/auth/register/",
                "login": "/auth/login/",
            },

            "clientes": {
                "listar": "/clientes/",
                "criar": "/clientes/criar/",
                "detalhe": "/clientes/<id>/",
                "atualizar": "/clientes/atualizar/<id>/",
                "deletar": "/clientes/deletar/<id>/",
            },

            "cardapio": {
                "listar": "/cardapio/",
                "criar": "/cardapio/criar/",
                "detalhe": "/cardapio/<id>/",
                "atualizar": "/cardapio/atualizar/<id>/",
                "deletar": "/cardapio/deletar/<id>/",
            },

            "pedidos": {
                "listar": "/pedidos/",
                "criar": "/pedidos/criar/",
                "detalhe": "/pedidos/<id>/",
                "atualizar": "/pedidos/atualizar/<id>/",
                "deletar": "/pedidos/deletar/<id>/",
            },

            "producao": {
                "listar": "/producao/",
                "criar": "/producao/criar/",
                "detalhe": "/producao/<id>/",
                "atualizar": "/producao/atualizar/<id>/",
                "deletar": "/producao/deletar/<id>/",
            },
        },

        "observacao": "Rotas (exceto auth, /cardapio/ e /cardapio/<id>) requerem JWT no header: Authorization: Bearer <token>",
    })