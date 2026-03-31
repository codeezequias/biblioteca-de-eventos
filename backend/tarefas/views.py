from django.http import JsonResponse
from .models import EventoAcademico

def listar_eventos(request):
    eventos = EventoAcademico.objects.all()
    return JsonResponse(list(eventos.values()), safe=False)