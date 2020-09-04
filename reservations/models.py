from django.db import models


class Reservation(models.Model):

    """ Reservation Model Definition """

    STATUS_PENDING = "pending"
    STATUS_CONFIRMED = "confirmed"
    STATUS_CANCELED = "canceled"
    STATUS_CHOICES = (
        (STATUS_PENDING, "Pending"),
        (STATUS_CONFIRMED, "Confirmed"),
        (STATUS_CANCELED, "Canceled"),
    )

    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    check_in = models.DateField()
    check_out = models.DateField()
    guest = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="reservations"
    )
    room = models.ForeignKey(
        "rooms.Room", on_delete=models.CASCADE, related_name="reservations"
    )

    def __str__(self):
        return f"{self.room} - {self.check_in}"