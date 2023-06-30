# Create your views here.
import json
from django.http import JsonResponse
from weather.tasks import obtener_datos_clima


def clima(request):
    try:
        result = obtener_datos_clima.delay().get()
        print(result)               
        return JsonResponse(result, safe=False)
    except Exception as e: 
        print(e)
        return JsonResponse({'error': 'Error al obtener los datos del clima'}, status=500)