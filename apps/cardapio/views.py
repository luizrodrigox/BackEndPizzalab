from django.http import JsonResponse
from .models import Pizza
import json
from django.views.decorators.csrf import csrf_exempt
from .forms import PizzaForm
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

        form = PizzaForm(data)

        if form.is_valid():
            pizza = form.save()
            return JsonResponse({"id": pizza.id})

        return JsonResponse(form.errors, status=400)

    return JsonResponse({"erro": "Método não permitido"}, status = 405)

def listar(request):
    if request.method == "GET":
        return JsonResponse(list(Pizza.objects.values()), safe = False)
    
    return JsonResponse({"erro": "Método não permitido"}, status = 405)


def detalhe(request, id):
    if request.method == "GET":
        pizza = Pizza.objects.filter(id = id).values().first()
        return JsonResponse(pizza or {"erro": "Não encontrada"})
    
    return JsonResponse({"erro": "Método não permitido"}, status = 405)

@csrf_exempt
def atualizar(request, id):
    if request.method == "PUT":

        if not verificar_token(request):
            return JsonResponse({"erro": "Não autorizado"}, status = 401)
        
        try:
            pizza = Pizza.objects.get(id=id)
        except Pizza.DoesNotExist:
            return JsonResponse({"erro": "Não encontrada"}, status = 404)

        try:
            data = json.loads(request.body)
        except:
            return JsonResponse({"erro": "JSON inválido"}, status = 400)

        form = PizzaForm(data, instance=pizza)

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
            Pizza.objects.get(id = id).delete()
            return JsonResponse({"msg": "Deletado"})
        except Pizza.DoesNotExist:
            return JsonResponse({"erro": "Não encontrada"})
    
    return JsonResponse({"erro": "Método não permitido"}, status = 405)