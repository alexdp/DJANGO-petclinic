"""Pet model – represents an animal registered at the clinic."""

from django.db import models

from clinic.models.owner import Owner


class Pet(models.Model):
    """A pet associated with an owner.

    Fields
    ------
    name : str
        Pet's name.
    birth_date : date
        Date the pet was born.
    type : str
        Species / type of the pet (e.g. "dog", "cat").
    owner : Owner
        The owner who registered this pet.
    """

    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    type = models.CharField(max_length=50)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name="pets")

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return f"{self.name} ({self.type})"
