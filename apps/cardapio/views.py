from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

cardapio = [
        {"id": 1,
         "nome": "Moda da Casa", 
         "Preco": 40.00},

        {"id": 2,
         "nome": "Frango com Catupiry", 
         "Preco": 30.00},

        {"id": 3,
         "nome": "Carne de Sol", 
         "Preco": 35.00},

        {"id": 4,
         "nome": "Calabresa", 
         "Preco": 30.00},

        {"id": 5,
         "nome": "Nordestina", 
         "Preco": 35.00},
    ]

def buscar_por_id(lista, id):
    for item in lista:
        if item.get("id") == id:
            return item
    return None

def listaCardapio(request):
    return JsonResponse(cardapio, safe=False)

def detalhePizza(request, id):
    pizza = buscar_por_id(cardapio, id)

    if pizza:
        return JsonResponse(pizza)

    return JsonResponse({"erro": "Pizza não encontrada"})