"""Repository for the Owner aggregate."""

from django.db.models import QuerySet

from clinic.models import Owner


class OwnerRepo:
    """Data-access object for :class:`~clinic.models.Owner`.

    All database interactions for owners are centralised here so that the
    service layer remains free of ORM specifics.
    """

    def get_all(self) -> QuerySet:
        """Return all owners ordered by last name, first name."""
        return Owner.objects.all()

    def get_by_id(self, owner_id: int) -> Owner:
        """Return the owner with the given primary key.

        Raises
        ------
        Owner.DoesNotExist
            If no owner with *owner_id* exists.
        """
        return Owner.objects.get(pk=owner_id)

    def save(self, owner: Owner) -> Owner:
        """Persist *owner* to the database and return the saved instance."""
        owner.save()
        return owner

    def delete(self, owner: Owner) -> None:
        """Delete *owner* from the database."""
        owner.delete()
