from rest_framework import serializers
from .models import Car

class CarListSerializer(serializers.ModelSerializer):
    class Meta():
        model = Car
        fields = ['id', 'name']

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name
        }


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['name', 'category', 'capacity', 'luggage', 'air_conditioning', 'transmission', 'mileage']