from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.HouseRule, models.Amenity, models.Facility)
class ItemAdmin(admin.ModelAdmin):

    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.rooms.count()


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Definition"""

    fieldsets = (
        (
            "Info",
            {
                "fields": (
                    "name",
                    "country",
                    "city",
                    "price",
                    "address",
                ),
            },
        ),
        (
            "Spaces",
            {
                "fields": ("guests", "beds", "bedrooms", "baths"),
            },
        ),
        (
            "Times",
            {
                "fields": (
                    "check_in",
                    "check_out",
                    "instant_book",
                ),
            },
        ),
        (
            "Detail",
            {
                "fields": ("house_rules", "amenities", "facilities", "room_type"),
            },
        ),
    )

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "address",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_photos",
        "total_reviews",
    )
    list_filter = (
        "host__superhost",
        "amenities",
        "facilities",
        "house_rules",
        "city",
        "country",
    )
    search_fields = ("^city", "^host__username")
    filter_horizontal = ("amenities", "facilities", "house_rules")

    def count_amenities(self, obj):
        return obj.amenities.count()

    def count_photos(self, obj):
        return obj.photos.count()


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Photo Admin Definition"""
