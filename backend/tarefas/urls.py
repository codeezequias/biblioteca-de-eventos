from django.urls import path
from .views import listar_eventos

urlpatterns = [
    path('eventos/', listar_eventos),
]