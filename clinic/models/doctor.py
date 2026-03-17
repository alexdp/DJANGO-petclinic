"""Doctor model – represents a doctor registered in the clinic."""

from django.db import models


class Doctor(models.Model):
    """A doctor registered in the clinic.

    Fields
    ------
    first_name : str
        Doctor's first name.
    last_name : str
        Doctor's last name.
    email : str
        Doctor's email address (unique).
    phone : str
        Doctor's contact phone number.
    """

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=30)

    class Meta:
        ordering = ["last_name", "first_name"]

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
