import json

from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from api.models import Breed
from api.serializers import BreedSerializer

BASE_URL = "breeds"
LIST_URL = f"{BASE_URL}-list"
DETAIL_URL = f"{BASE_URL}-detail"


class TestBreedViewSet(TestCase):
    def setUp(self) -> None:
        self.breed1 = Breed.objects.create(
            name="B1",
            size="TINY",
            friendliness=1,
            train_ability=1,
            shedding_amount=1,
            exercise_needs=1,
        )
        self.breed2 = Breed.objects.create(
            name="B2",
            size="TINY",
            friendliness=1,
            train_ability=1,
            shedding_amount=1,
            exercise_needs=1,
        )

    def test_retrieve_all_objects(self):
        response = self.client.get(path=reverse(LIST_URL))
        response_data = response.json()
        expected_data = BreedSerializer(Breed.objects.all(), many=True).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Breed.objects.count())
        self.assertEqual(response_data, expected_data)

    def test_post_object(self):
        breed3_data = {
            "name": "B3",
            "size": "TINY",
            "friendliness": 1,
            "train_ability": 1,
            "shedding_amount": 1,
            "exercise_needs": 1,
        }
        self.assertEqual(Breed.objects.count(), 2)
        response = self.client.post(path=reverse(LIST_URL), data=breed3_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Breed.objects.count(), 3)

    def test_get_existing_object_success(self):
        pk = 1
        response = self.client.get(path=reverse(DETAIL_URL, kwargs={"pk": pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["name"], self.breed1.name)

    def test_get_not_existing_object_success(self):
        pk = 3
        response = self.client.get(path=reverse(DETAIL_URL, kwargs={"pk": pk}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_existing_object(self):
        updated_data = {"name": "B100"}
        pk = 1
        content_type = "application/json"
        response = self.client.patch(
            path=reverse(DETAIL_URL, kwargs={"pk": pk}),
            data=updated_data,
            content_type=content_type,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Breed.objects.get(id=pk).name, updated_data["name"])

    def test_update_not_existing_object(self):
        updated_data = {"name": "B100"}
        pk = 3
        content_type = "application/json"
        response = self.client.patch(
            path=reverse(DETAIL_URL, kwargs={"pk": pk}),
            data=updated_data,
            content_type=content_type,
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_existing_object(self):
        pk = 1
        self.assertEqual(Breed.objects.count(), 2)
        response = self.client.delete(path=reverse(DETAIL_URL, kwargs={"pk": pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Breed.objects.count(), 1)

    def test_delete_not_existing_object(self):
        pk = 3
        response = self.client.delete(path=reverse(DETAIL_URL, kwargs={"pk": pk}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
