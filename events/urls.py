from django.urls import path
from .views import event_list

urlpatterns = [
    path('list/', event_list, name='events'),
]