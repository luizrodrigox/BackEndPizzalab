from django.http import JsonResponse
from .models import Pedido
from apps.clientes.models import Cliente
from apps.cardapio.models import Pizza
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def criar(request):
    if request.method == "POST":
        data = json.loads(request.body)

        cliente = Cliente.objects.get(id = data["cliente_id"])
        pedido = Pedido.objects.create(
            cliente = cliente,
            status = data["status"]
        )

        pizzas = Pizza.objects.filter(id__in = data["pizzas_ids"])
        pedido.pizzas.set(pizzas)

        return JsonResponse({"id": pedido.id})
    
    return JsonResponse({"erro": "Método não permitido"}, status = 405)


def listar(request):
    if request.method == "GET":
        pedidos = []
        for p in Pedido.objects.all():
            pedidos.append({
                "id": p.id,
                "cliente": p.cliente.nome,
                "pizzas": [pizza.nome for pizza in p.pizzas.all()],
                "status": p.status
            })
        return JsonResponse(pedidos, safe = False)
    
    return JsonResponse({"erro": "Método não permitido"}, status = 405)


def detalhe(request, id):
    if request.method == "GET":
        try:
            p = Pedido.objects.get(id = id)
            return JsonResponse({
                "id": p.id,
                "cliente": p.cliente.nome,
                "pizzas": [pizza.nome for pizza in p.pizzas.all()],
                "status": p.status
            })
        except Pedido.DoesNotExist:
            return JsonResponse({"erro": "Não encontrado"})
    
    return JsonResponse({"erro": "Método não permitido"}, status = 405)

@csrf_exempt
def atualizar(request, id):
    if request.method == "PUT":
        try:
            data = json.loads(request.body)
            pedido = Pedido.objects.get(id = id)

            if "cliente_id" in data:
                pedido.cliente = Cliente.objects.get(id = data["cliente_id"])

            if "status" in data:
                pedido.status = data["status"]

            pedido.save()

            if "pizzas_ids" in data:
                pizzas = Pizza.objects.filter(id__in = data["pizzas_ids"])
                pedido.pizzas.set(pizzas)

            return JsonResponse({"msg": "Atualizado"})
        except Pedido.DoesNotExist:
            return JsonResponse({"erro": "Não encontrado"})
    
    return JsonResponse({"erro": "Método não permitido"}, status = 405)

@csrf_exempt
def deletar(request, id):
    if request.method == "DELETE":
        try:
            Pedido.objects.get(id = id).delete()
            return JsonResponse({"msg": "Deletado"})
        except Pedido.DoesNotExist:
            return JsonResponse({"erro": "Não encontrado"})
    
    return JsonResponse({"erro": "Método não permitido"}, status = 405)