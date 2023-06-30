import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print('entra a connect')        
        await self.channel_layer.group_add("notifications", self.channel_name)
        await self.accept()
        

    async def disconnect(self, close_code):        
        print('disconect')
        await self.channel_layer.group_discard("notifications", self.channel_name)


    async def receive(self, text_data=None, bytes_data=None):
        # Aquí puedes manejar los mensajes recibidos desde el frontend
        print('Mensaje recibido del frontend:', text_data)
        channel_layer = get_channel_layer()
        await channel_layer.group_send("notifications", {
            "type": "notification_message",
            "content": "Mensaje de notificación"
        })
    
    async def notification_message(self, event):
        # Envia el mensaje de notificación al cliente
        await self.send(text_data=event["content"])
        