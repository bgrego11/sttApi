from django.shortcuts import render
from rest_framework import viewsets
from .serializers import EventsSerializer
from .models import Event

# Create your views here.
def index(request):
    return False

class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Event.objects.all().order_by('-created_date')
    serializer_class = EventsSerializer