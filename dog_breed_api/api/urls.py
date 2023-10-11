from rest_framework.routers import SimpleRouter


from .views import DogViewSet, BreedViewSet

router = SimpleRouter()
router.register(prefix=r"dogs", viewset=DogViewSet, basename="dogs")
router.register(prefix=r"breeds", viewset=BreedViewSet, basename="breeds")

urlpatterns = [] + router.urls
