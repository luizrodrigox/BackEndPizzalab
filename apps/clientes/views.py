from django.http import JsonResponse
from .models import Cliente
import json
from django.views.decorators.csrf import csrf_exempt
from .forms import ClienteForm
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

        form = ClienteForm(data)

        if form.is_valid():
            cliente = form.save()
            return JsonResponse({"id": cliente.id})

        return JsonResponse(form.errors, status=400)

    return JsonResponse({"erro": "Método não permitido"}, status = 405)


def listar(request):
    if request.method == "GET":

        if not verificar_token(request):
            return JsonResponse({"erro": "Não autorizado"}, status = 401)
        
        return JsonResponse(list(Cliente.objects.values()), safe = False)
    
    return JsonResponse({"erro": "Método não permitido"}, status = 405)


def detalhe(request, id):
    if request.method == "GET":

        if not verificar_token(request):
            return JsonResponse({"erro": "Não autorizado"}, status = 401)
        
        cliente = Cliente.objects.filter(id = id).values().first()
        return JsonResponse(cliente or {"erro": "Não encontrado"})
    
    return JsonResponse({"erro": "Método não permitido"}, status = 405)

@csrf_exempt
def atualizar(request, id):
    if request.method == "PUT":

        if not verificar_token(request):
            return JsonResponse({"erro": "Não autorizado"}, status = 401)
        
        try:
            cliente = Cliente.objects.get(id=id)
        except Cliente.DoesNotExist:
            return JsonResponse({"erro": "Não encontrado"}, status = 404)

        try:
            data = json.loads(request.body)
        except:
            return JsonResponse({"erro": "JSON inválido"}, status = 400)

        form = ClienteForm(data, instance=cliente)

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
            Cliente.objects.get(id = id).delete()
            return JsonResponse({"msg": "Deletado"})
        except Cliente.DoesNotExist:
            return JsonResponse({"erro": "Não encontrado"})
    
    return JsonResponse({"erro": "Método não permitido"}, status = 405)