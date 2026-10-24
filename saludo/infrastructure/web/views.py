import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from saludo.domain.persona import Persona
from saludo.application.services.saludar_service import SaludarService

use_case = SaludarService()

@csrf_exempt #petuciones q no vengan de web
def saludar_view(request):
    data = json.loads(request.body)
    mensaje = use_case.saludar(Persona(data["nombre"]))
    return JsonResponse({"mensaje": mensaje})