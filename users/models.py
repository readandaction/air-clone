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

    bio = models.TextField(default="", null=True, blank=True)
    avatar = models.ImageField(blank=True, null=True)
    gender = models.CharField(
        chices=GENDER_CHOICES, max_length=10, null=True, blank=True
    )
