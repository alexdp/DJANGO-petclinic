"""Owner model – represents a pet owner registered in the clinic."""

from django.db import models


class Owner(models.Model):
    """A person who owns one or more pets.

    Fields
    ------
    first_name : str
        Owner's first name.
    last_name : str
        Owner's last name.
    email : str
        Owner's email address (unique).
    phone : str
        Owner's contact phone number.
    """

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=30)

    class Meta:
        ordering = ["last_name", "first_name"]

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
