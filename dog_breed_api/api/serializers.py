from .models import Dog, Breed
from rest_framework import serializers


class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = "__all__"


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = "__all__"
