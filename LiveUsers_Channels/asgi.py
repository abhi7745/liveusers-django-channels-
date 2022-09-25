"""
ASGI config for LiveUsers_Channels project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter, URLRouter # channels setup
from channels.auth import AuthMiddlewareStack # channels setup
import accounts.routing # channels setup
         
         

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LiveUsers_Channels.settings')

# application = get_asgi_application()

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket' : AuthMiddlewareStack(  
        URLRouter(
                accounts.routing.websocket_urlpatters
        )
    )
})
