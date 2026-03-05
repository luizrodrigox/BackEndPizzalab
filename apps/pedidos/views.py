from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

pedidos = [
        {"id": 1,
         "cliente": "João Silva",
         "total": 70.00},

        {"id": 2,
         "cliente": "Maria Souza",
         "total": 40.00},
    ]

def buscar_por_id(lista, id):
    for item in lista:
        if item.get("id") == id:
            return item
    return None

def listaPedidos(request):
    return JsonResponse(pedidos, safe=False)

def detalhePedido(request, id):
    pedido = buscar_por_id(pedidos, id)

    if pedido:
        return JsonResponse(pedido)

    return JsonResponse({"erro": "Pedido não encontrado"})