from django.http import Http404
from rest_framework import status
from rest_framework.generics import (
    GenericAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
    CreateAPIView,
)
from rest_framework.mixins import (
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    CreateModelMixin,
)
from rest_framework.response import Response
from .models import Dog, Breed
from .serializers import DogSerializer, BreedSerializer
from rest_framework.views import APIView

# APIView
# class DogDetail(APIView):
#     def get_object(self, pk):
#         try:
#             dog = Dog.objects.get(id=pk)
#         except Dog.DoesNotExist:
#             raise Http404
#         else:
#             return dog
#
#     def get(self, request, pk):
#         dog = self.get_object(pk)
#         serializer = DogSerializer(dog)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         dog = self.get_object(pk=pk)
#         serializer = DogSerializer(dog, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         dog = self.get_object(pk=pk)
#         dog.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# class DogList(APIView):
#     def get(self, request):
#         dogs = Dog.objects.all()
#         if dogs:
#             serializer = DogSerializer(dogs, many=True)
#             return Response(serializer.data)
#         return Http404
#
#     def post(self, request):
#         serializer = DogSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class BreedDetail(APIView):
#     def get_object(self, pk):
#         try:
#             breed = Breed.objects.get(id=pk)
#         except Breed.DoesNotExist:
#             return Http404
#         else:
#             return breed
#
#     def get(self, request, pk):
#         breed = self.get_object(pk=pk)
#         serializer = BreedSerializer(breed)
#         return Response(data=serializer.data)
#
#     def put(self, request, pk):
#         serializer = BreedSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         breed = self.get_object(pk=pk)
#         breed.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# class BreedList(APIView):
#     def get(self, request):
#         breeds = Breed.objects.all()
#         if breeds:
#             serializer = BreedSerializer(breeds, many=True)
#             return Response(serializer.data)
#         return Response(breeds.errors, status=status.HTTP_404_NOT_FOUND)
#
#     def post(self, request):
#         serializer = BreedSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)


# # Mixins and GenericAPIView
# class DogDetail(
#     RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericAPIView
# ):
#     queryset = Dog.objects.all()
#     serializer_class = DogSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
#
#
# class DogList(ListModelMixin, CreateModelMixin, GenericAPIView):
#     queryset = Dog.objects.all()
#     serializer_class = DogSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#
# class BreedDetail(
#     RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericAPIView
# ):
#     queryset = Breed.objects.all()
#     serializer_class = BreedSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
#
#
# class BreedList(ListModelMixin, CreateModelMixin, GenericAPIView):
#     queryset = Breed.objects.all()
#     serializer_class = BreedSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# RetrieveUpdateDestroyAPIView, ListAPIView, CreateAPIView


class DogDetail(RetrieveUpdateDestroyAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer


class DogList(ListAPIView, CreateAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer


class BreedDetail(RetrieveUpdateDestroyAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


class BreedList(ListAPIView, CreateAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
