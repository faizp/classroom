from django.urls import path
from .views import peer

urlpatterns = [
    path('<str:room_name>/', peer, name='peer'),
]