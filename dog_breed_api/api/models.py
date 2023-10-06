from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Breed(models.Model):
    TINY = "TINY"
    SMALL = "SMALL"
    MEDIUM = "MEDIUM"
    LARGE = "LARGE"

    SIZE_CHOICES = [
        (TINY, "tiny"),
        (SMALL, "small"),
        (MEDIUM, "medium"),
        (LARGE, "large"),
    ]

    FEMALE = "F"
    MALE = "M"

    GENDER_CHOICES = [(FEMALE, "female"), (MALE, "male")]

    name = models.CharField(max_length=20)
    size = models.CharField(max_length=6, choices=SIZE_CHOICES)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    color = models.CharField(max_length=20)
    favourite_food = models.CharField(max_length=30)
    favourite_toy = models.CharField(max_length=30)


class Dog(models.Model):
    name = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    breed = models.ForeignKey(Breed, on_delete=models.SET_NULL, null=True)
    friendliness = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    train_ability = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    shedding_amount = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    exercise_needs = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
