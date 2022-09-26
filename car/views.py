from rest_framework.generics import ListAPIView, DestroyAPIView, CreateAPIView, RetrieveUpdateAPIView
from .serializers import CarListSerializer, CarSerializer
from .models import Car


class CarListProv(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarListSerializer


class CarCreate(CreateAPIView):
    serializer_class = CarSerializer


class CarDetailProv(RetrieveUpdateAPIView):
    serializer_class = CarSerializer 
    queryset = Car.objects.all()  
    lookup_field = 'id'

class CarDeleteProv(DestroyAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
    lookup_field = "id"

