from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from restonauta.consumers import NotificationConsumer



def enviar_notificacion(notification):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)("notifications", {
        "type": "render",
        "content": notification
    })
   