from django.http import JsonResponse
from .models import Pedido
from apps.clientes.models import Cliente
from apps.cardapio.models import Pizza
import json
from django.views.decorators.csrf import csrf_exempt
from .forms import PedidoForm

@csrf_exempt
def criar(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
        except:
            return JsonResponse({"erro": "JSON inválido"}, status = 400)

        try:
            cliente = Cliente.objects.get(id=data["cliente_id"])
        except Cliente.DoesNotExist:
            return JsonResponse({"erro": "Cliente não encontrado"}, status = 404)

        form = PedidoForm({
            "cliente": cliente.id,
            "status": data.get("status")
        })

        if form.is_valid():
            pedido = form.save()

            pizzas = Pizza.objects.filter(id__in=data.get("pizzas_ids", []))
            pedido.pizzas.set(pizzas)

            return JsonResponse({"id": pedido.id})

        return JsonResponse(form.errors, status = 400)

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
            pedido = Pedido.objects.get(id=id)
        except Pedido.DoesNotExist:
            return JsonResponse({"erro": "Não encontrado"}, status = 404)

        try:
            data = json.loads(request.body)
        except:
            return JsonResponse({"erro": "JSON inválido"}, status = 400)

        form = PedidoForm({
            "cliente": data.get("cliente_id", pedido.cliente.id),
            "status": data.get("status", pedido.status)
        }, instance=pedido)

        if form.is_valid():
            form.save()

            if "pizzas_ids" in data:
                pizzas = Pizza.objects.filter(id__in=data["pizzas_ids"])
                pedido.pizzas.set(pizzas)

            return JsonResponse({"msg": "Atualizado"})

        return JsonResponse(form.errors, status = 400)

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