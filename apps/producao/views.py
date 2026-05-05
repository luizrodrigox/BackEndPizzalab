from django.http import JsonResponse
from .models import Producao
from apps.pedidos.models import Pedido
import json
from django.views.decorators.csrf import csrf_exempt
from .forms import ProducaoForm
from utils.auth import verificar_token

@csrf_exempt
def criar(request):
    if request.method == "POST":

        if not verificar_token(request):
            return JsonResponse({"erro": "Não autorizado"}, status = 401)
        
        try:
            data = json.loads(request.body)
        except:
            return JsonResponse({"erro": "JSON inválido"}, status = 400)

        try:
            pedido = Pedido.objects.get(id=data["pedido_id"])
        except Pedido.DoesNotExist:
            return JsonResponse({"erro": "Pedido não encontrado"}, status = 404)

        form = ProducaoForm({
            "pedido": pedido.id,
            "status": data.get("status")
        })

        if form.is_valid():
            prod = form.save()
            return JsonResponse({"id": prod.id})

        return JsonResponse(form.errors, status = 400)

    return JsonResponse({"erro": "Método não permitido"}, status = 405)


def listar(request):
    if request.method == "GET":

        if not verificar_token(request):
            return JsonResponse({"erro": "Não autorizado"}, status = 401)
        
        return JsonResponse(list(Producao.objects.values()), safe = False)
    
    return JsonResponse({"erro": "Método não permitido"}, statu = 405)


def detalhe(request, id):
    if request.method == "GET":

        if not verificar_token(request):
            return JsonResponse({"erro": "Não autorizado"}, status = 401)
        
        try:
            prod = Producao.objects.get(id = id)
            return JsonResponse({
                "id": prod.id,
                "pedido_id": prod.pedido.id,
                "status": prod.status
            })
        except Producao.DoesNotExist:
            return JsonResponse({"erro": "Não encontrado"})
    
    return JsonResponse({"erro": "Método não permitido"}, status = 405)

@csrf_exempt
def atualizar(request, id):
    if request.method == "PUT":

        if not verificar_token(request):
            return JsonResponse({"erro": "Não autorizado"}, status = 401)
        
        try:
            prod = Producao.objects.get(id=id)
        except Producao.DoesNotExist:
            return JsonResponse({"erro": "Não encontrado"}, status = 404)

        try:
            data = json.loads(request.body)
        except:
            return JsonResponse({"erro": "JSON inválido"}, status = 400)

        form = ProducaoForm({
            "pedido": prod.pedido.id,
            "status": data.get("status")
        }, instance=prod)

        if form.is_valid():
            form.save()
            return JsonResponse({"msg": "Atualizado"})

        return JsonResponse(form.errors, status = 400)

    return JsonResponse({"erro": "Método não permitido"}, status = 405)

@csrf_exempt
def deletar(request, id):
    if request.method == "DELETE":

        if not verificar_token(request):
            return JsonResponse({"erro": "Não autorizado"}, status = 401)
        
        try:
            Producao.objects.get(id = id).delete()
            return JsonResponse({"msg": "Deletado"})
        except Producao.DoesNotExist:
            return JsonResponse({"erro": "Não encontrado"})
    
    return JsonResponse({"erro": "Método não permitido"}, status = 405)