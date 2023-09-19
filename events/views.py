from django.http import JsonResponse
from .models import Event

def event_list(request):
    return JsonResponse([event.get_data for event in Event.objects.all()], safe=False)