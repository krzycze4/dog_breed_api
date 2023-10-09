from django.urls import path
from .views import DogDetail, DogList

urlpatterns = [
    path("dogs/<int:pk>", DogDetail.as_view(), name="dog_view"),
    path("dogs/", DogList.as_view(), name="dogs_view"),
]
