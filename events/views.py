from django.http import JsonResponse
from .models import Event

def event_list(request):
    events_list = [
            {
                'event': event.get_data
            }
            for event in Event.objects.all()
        ]
    return JsonResponse(events_list, safe=False)