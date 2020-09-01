from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"
    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )
    LANGUAGE_KOREAN = "kr"
    LANGUAGE_USD = "us"
    LANGUAGE_CHOICES = ((LANGUAGE_KOREAN, "Kr"), (LANGUAGE_USD, "USD"))
    CURRENCY_KOREAN = "kr"
    CURRENCY_USD = "usd"
    CURRENCY_CHOICES = ((CURRENCY_KOREAN, "Kr"), (CURRENCY_USD, "USD"))

    bio = models.TextField(default="", null=True, blank=True)
    avatar = models.ImageField(blank=True, null=True)
    gender = models.CharField(
        choices=GENDER_CHOICES, max_length=10, null=True, blank=True
    )
    language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES, null=True)
    currency = models.CharField(max_length=10, choices=CURRENCY_CHOICES, null=True)
    superhost = models.BooleanField(default=False)