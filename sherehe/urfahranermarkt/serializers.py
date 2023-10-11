from rest_framework import serializers
from .models import *


# Serializers to for each model to allow easy data type conversion


class DustbinsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dustbins
        fields = '__all__'
class FoodAreasSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodAreas
        fields = '__all__'


class FoodStallsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodStalls
        fields = '__all__'


class InfoPointsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoPoints
        fields = '__all__'


class KidsArenaSerializer(serializers.ModelSerializer):
    class Meta:
        model = KidsArena
        fields = '__all__'


class ShopsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shops
        fields = '__all__'


class SouvenirsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Souvenirs
        fields = '__all__'


class StagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stages
        fields = '__all__'


class TrampolineParkSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrampolinePark
        fields = '__all__'


class WashroomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Washrooms
        fields = '__all__'
