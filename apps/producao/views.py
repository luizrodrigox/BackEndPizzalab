from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

producao = [
        {"id": 1,
         "pedido_id": 1,
         "status": "Em preparo"},

        {"id": 2,
         "pedido_id": 2,
         "status": "Saiu para entrega"},
    ]

def buscar_por_id(lista, id):
    for item in lista:
        if item.get("id") == id:
            return item
    return None

def listaProducao(request):
    return JsonResponse(producao, safe=False)

def detalheProducao(request, id):
    status = buscar_por_id(producao, id)

    if status:
        return JsonResponse(status)

    return JsonResponse({"erro": "Status não encontrado"})