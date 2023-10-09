from django.urls import path
from .views import DogDetail, DogList, BreedDetail, BreedList

urlpatterns = [
    path("dogs/<int:pk>", DogDetail.as_view(), name="dog_view"),
    path("dogs/", DogList.as_view(), name="dogs_view"),
    path("breeds/<int:pk>", BreedDetail.as_view(), name="breed_view"),
    path("breeds/", BreedList.as_view(), name="breeds_view"),
]
