from django.urls import path
from .views import DogDetail

urlpatterns = [path("dogs/<int:pk>", DogDetail.as_view(), name="get_dog")]
