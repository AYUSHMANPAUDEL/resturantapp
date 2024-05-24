from django.urls import path
from home import consumers
websocket_urlpatterns = [
  path('ws/sc',consumers.mysyncconsumer.as_asgi()),
  path('ws/ac',consumers.myasyncconsumer.as_asgi()),
]