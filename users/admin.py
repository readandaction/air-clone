from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (
            "Detail",
            {
                "fields": (
                    "bio",
                    "avatar",
                    "gender",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )
