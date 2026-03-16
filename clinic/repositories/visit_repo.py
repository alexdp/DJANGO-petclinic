"""Repository for the Visit aggregate."""

from django.db.models import QuerySet

from clinic.models import Pet, Visit


class VisitRepo:
    """Data-access object for :class:`~clinic.models.Visit`.

    Centralises all ORM interactions related to veterinary visits.
    """

    def get_all(self) -> QuerySet:
        """Return all visits with their related pet and owner pre-fetched."""
        return Visit.objects.select_related("pet", "pet__owner").all()

    def get_by_id(self, visit_id: int) -> Visit:
        """Return the visit with the given primary key.

        Raises
        ------
        Visit.DoesNotExist
            If no visit with *visit_id* exists.
        """
        return Visit.objects.select_related("pet", "pet__owner").get(pk=visit_id)

    def get_by_pet(self, pet: Pet) -> QuerySet:
        """Return all visits for *pet*, most recent first."""
        return Visit.objects.filter(pet=pet).select_related("pet", "pet__owner")

    def save(self, visit: Visit) -> Visit:
        """Persist *visit* to the database and return the saved instance."""
        visit.save()
        return visit

    def delete(self, visit: Visit) -> None:
        """Delete *visit* from the database."""
        visit.delete()
