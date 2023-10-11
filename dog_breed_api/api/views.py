from rest_framework.viewsets import ModelViewSet

from .models import Dog, Breed
from .serializers import DogSerializer, BreedSerializer


class DogViewSet(ModelViewSet):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer


class BreedViewSet(ModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
