import requests
from celery import shared_task
from restonauta.settings import TOMORROWIO_API_KEY, TOMORROWIO_URL, TOMORROWIO_COORDINATES, TOMORROWIO_TIME_RANGE

@shared_task
def obtener_datos_clima():
    # Realiza la llamada a la API del clima
   
    try:
        response = requests.get(
            f'{TOMORROWIO_URL}/timelines?location={TOMORROWIO_COORDINATES}&fields=temperature&timesteps={TOMORROWIO_TIME_RANGE}&units=metric&apikey={TOMORROWIO_API_KEY}')
        data = response.json()        
        return data
    except Exception as e:
        print(f'obtener_datos_clima: {e}')
        return None