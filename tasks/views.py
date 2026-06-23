from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Tarea

def listar_tareas(request):
    tareas = list(Tarea.objects.values())
    return JsonResponse({'tareas': tareas})

@csrf_exempt
@require_http_methods(["POST"])
def crear_tarea(request):
    data = json.loads(request.body)
    tarea = Tarea.objects.create(
        titulo=data['titulo'],
        descripcion=data.get('descripcion', ''),
    )
    return JsonResponse({'id': tarea.id, 'titulo': tarea.titulo}, status=201)