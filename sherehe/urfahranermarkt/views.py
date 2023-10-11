from _ast import Return

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .serializers import *

# Create your views here.

class DustbinsList(generics.ListAPIView):
    queryset = Dustbins.objects.all()
    serializer_class = DustbinsSerializer

class FoodAreasList(generics.ListAPIView):
    queryset = FoodAreas.objects.all()
    serializer_class = FoodAreasSerializer

class FoodStallsList(generics.ListAPIView):
    queryset = FoodStalls.objects.all()
    serializer_class = FoodStallsSerializer

class InfoPointsList(generics.ListAPIView):
    queryset = InfoPoints.objects.all()
    serializer_class = InfoPointsSerializer

class KidsArenaList(generics.ListAPIView):
    queryset = KidsArena.objects.all()
    serializer_class = KidsArenaSerializer

class ShopsList(generics.ListAPIView):
    queryset = Shops.objects.all()
    serializer_class = ShopsSerializer

class SouvenirsList(generics.ListAPIView):
    queryset = Souvenirs.objects.all()
    serializer_class = SouvenirsSerializer

class StagesList(generics.ListAPIView):
    queryset = Stages.objects.all()
    serializer_class = StagesSerializer

class TrampolineParkList(generics.ListAPIView):
    queryset = TrampolinePark.objects.all()
    serializer_class = TrampolineParkSerializer

class WashroomsList(generics.ListAPIView):
    queryset = Washrooms.objects.all()
    serializer_class = WashroomsSerializer

def index(request):
    return HttpResponse("Hello, You are at the Festival App Index")

def map_view(request):
    return render(request, 'map.html')
