import os

from channels.routing import ProtocolTypeRouter, URLRouter

from django.core.asgi import get_asgi_application

from core.middlewares.socket_middleware import AuthSocketMiddleware

from .routing import websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'configs.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthSocketMiddleware(URLRouter(websocket_urlpatterns))
})
