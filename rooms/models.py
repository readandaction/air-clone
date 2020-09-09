from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models


class AbstactItem(core_models.TimeStampedModel):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class RoomType(AbstactItem):
    """ RoomType Model definition """

    class Meta:
        verbose_name = "Room Type"


class HouseRule(AbstactItem):
    """ House Rule Model definition """

    class Meta:
        verbose_name = "House Rule"


class Amenity(AbstactItem):

    """ Amenity Model definition """

    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstactItem):

    """ facility Model definition """

    class Meta:
        verbose_name_plural = "Facilties"


class Photo(core_models.TimeStampedModel):

    """ Photo Model definition """

    caption = models.CharField(max_length=30)
    file = models.ImageField()
    room = models.ForeignKey("Room", related_name="photos", on_delete=models.CASCADE)


class Room(core_models.TimeStampedModel):

    """Room Model Definition"""

    name = models.CharField(max_length=40)
    description = models.TextField(null=True)
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(
        user_models.User, on_delete=models.CASCADE, related_name="rooms"
    )
    room_type = models.ForeignKey(
        RoomType, null=True, on_delete=models.SET_NULL, related_name="rooms"
    )
    house_rules = models.ManyToManyField(HouseRule, blank=True, related_name="rooms")
    amenities = models.ManyToManyField(Amenity, blank=True, related_name="rooms")
    facilities = models.ManyToManyField(Facility, blank=True, related_name="rooms")

    def __str__(self):
        return self.name

    def total_reviews(self):
        all_reviews = self.reviews.all()
        all_ratings = 0
        if len(all_reviews) > 0:
            for review in all_reviews:
                all_ratings += review.rating_average()
            return all_ratings / len(all_reviews)
        return 0