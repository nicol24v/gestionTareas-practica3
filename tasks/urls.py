from django.urls import path
from . import views

urlpatterns = [
    path('tareas/', views.listar_tareas),
    path('tareas/crear/', views.crear_tarea),
]