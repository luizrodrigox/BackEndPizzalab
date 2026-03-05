from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

clientes = [
        {"id": 1,
         "nome": "João Silva",
         "telefone": "99999-9999"},

        {"id": 2,
         "nome": "Maria Souza",
         "telefone": "88888-8888"},
    ]

def buscar_por_id(lista, id):
    for item in lista:
        if item.get("id") == id:
            return item
    return None

def listaClientes(request):
    return JsonResponse(clientes, safe=False)

def detalheCliente(request, id):
    cliente = buscar_por_id(clientes, id)

    if cliente:
        return JsonResponse(cliente)

    return JsonResponse({"erro": "Cliente não encontrado"})   