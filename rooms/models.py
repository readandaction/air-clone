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
    room = models.ForeignKey("Room", on_delete=models.CASCADE)


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
    host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    room_type = models.ForeignKey(RoomType, null=True, on_delete=models.SET_NULL)
    house_rules = models.ManyToManyField(HouseRule, blank=True)
    amenities = models.ManyToManyField(Amenity, blank=True)
    facilities = models.ManyToManyField(Facility, blank=True)

    def __str__(self):
        return self.name