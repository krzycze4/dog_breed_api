import json

from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from api.models import Dog, Breed

from api.serializers import DogSerializer

BASE_URL = "dogs"
LIST_URL = f"{BASE_URL}-list"
DETAIL_URL = f"{BASE_URL}-detail"


class TestDogViewSet(TestCase):
    def setUp(self) -> None:
        breed = Breed.objects.create(
            name="Breed",
            size="TINY",
            friendliness=1,
            train_ability=1,
            shedding_amount=1,
            exercise_needs=1,
        )
        self.dog1 = Dog.objects.create(
            name="Dog1",
            age=1,
            breed=breed,
            color="c",
            gender="M",
            favourite_food="f",
            favourite_toy="t",
        )
        self.dog2 = Dog.objects.create(
            name="Dog2",
            age=1,
            breed=breed,
            color="c",
            gender="M",
            favourite_food="f",
            favourite_toy="t",
        )

    def test_retrieve_all_objects_success(self):
        response = self.client.get(path=reverse(LIST_URL))

        response_data = response.json()
        expected_data = DogSerializer(Dog.objects.all(), many=True).data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_data, expected_data)
        self.assertEqual(len(response_data), 2)

    def test_post_object_success(self):
        dog3_data_to_create = {
            "name": "Dog3",
            "age": 1,
            "breed": 1,
            "color": "c",
            "gender": "M",
            "favourite_food": "f",
            "favourite_toy": "t",
        }
        response = self.client.post(path=reverse(LIST_URL), data=dog3_data_to_create)
        dog3_data_from_db = Dog.objects.last()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(dog3_data_from_db.name, dog3_data_to_create["name"])
        self.assertEqual(Dog.objects.count(), 3)

    def test_get_single_existing_object_success(self):
        pk = 1
        response = self.client.get(path=reverse(DETAIL_URL, kwargs={"pk": pk}))
        response_json = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.dog1.name, response_json["name"])

    def test_get_single_not_existing_object_failed(self):
        pk = 3
        response = self.client.get(path=reverse(DETAIL_URL, kwargs={"pk": pk}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_existing_single_object(self):
        self.assertEqual(Dog.objects.count(), 2)
        pk = 1
        response = self.client.delete(path=reverse(DETAIL_URL, kwargs={"pk": pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Dog.objects.count(), 1)

    def test_delete_not_existing_object(self):
        self.assertEqual(Dog.objects.count(), 2)
        pk = 3
        response = self.client.delete(path=reverse(DETAIL_URL, kwargs={"pk": pk}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(Dog.objects.count(), 2)

    def test_update_existing_object(self):
        updated_name = {"name": "Doggo"}
        updated_json = json.dumps(updated_name)
        pk = 1
        content_type = "application/json"
        self.assertEqual(Dog.objects.first().name, self.dog1.name)
        response = self.client.patch(
            path=reverse(DETAIL_URL, kwargs={"pk": pk}),
            data=updated_json,
            content_type=content_type,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Dog.objects.first().name, updated_name["name"])
