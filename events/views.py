from django.shortcuts import render
from rest_framework import viewsets
from .serializers import EventsSerializer
from .models import Event
from datetime import datetime, date, time

# Create your views here.
def index(request):
    return False

class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    today = datetime.combine(date.today(), time())
    queryset = Event.objects.filter(logdate__gte=today).order_by('created_date')
    serializer_class = EventsSerializer