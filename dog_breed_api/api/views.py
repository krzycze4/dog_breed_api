from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from .models import Dog
from .serializers import DogSerializer
from rest_framework.views import APIView


class DogDetail(APIView):
    def get_object(self, pk):
        try:
            dog = Dog.objects.get(id=pk)
        except Dog.DoesNotExist:
            raise Http404
        else:
            return dog

    def get(self, request, pk):
        dog = self.get_object(pk)
        serializer = DogSerializer(dog)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        dog = self.get_object(pk=pk)
        serializer = DogSerializer(dog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        dog = self.get_object(pk=pk)
        dog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
