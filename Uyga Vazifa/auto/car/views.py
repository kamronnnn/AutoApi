from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Car
from .serializers import CarSerializers

# Create your views here.


class CarApiView(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializers


class CarRetrieveApiView(RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializers
