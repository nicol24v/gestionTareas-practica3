from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from .models import Tarea
import json

class TareaModelTest(TestCase):
    def test_crear_tarea(self):
        tarea = Tarea.objects.create(titulo='Test tarea')
        self.assertEqual(tarea.titulo, 'Test tarea')
        self.assertEqual(tarea.estado, 'pendiente')

    def test_str_tarea(self):
        tarea = Tarea.objects.create(titulo='Mi tarea')
        self.assertEqual(str(tarea), 'Mi tarea')

class TareaAPITest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_listar_tareas_vacio(self):
        response = self.client.get('/tareas/')
        self.assertEqual(response.status_code, 200)

    def test_crear_tarea_api(self):
        response = self.client.post(
            '/tareas/crear/',
            data=json.dumps({'titulo': 'Nueva tarea'}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)