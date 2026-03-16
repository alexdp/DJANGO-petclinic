"""Visit model – records a veterinary visit for a pet."""

from django.db import models

from clinic.models.pet import Pet


class Visit(models.Model):
    """A single veterinary visit for a pet.

    Fields
    ------
    pet : Pet
        The pet that was seen.
    visit_date : date
        Date of the visit.
    description : str
        Notes or description of the visit.
    """

    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name="visits")
    visit_date = models.DateField()
    description = models.TextField()

    class Meta:
        ordering = ["-visit_date"]

    def __str__(self) -> str:
        return f"Visit for {self.pet} on {self.visit_date}"
