"""Repository for the Pet aggregate."""

from django.db.models import QuerySet

from clinic.models import Owner, Pet


class PetRepo:
    """Data-access object for :class:`~clinic.models.Pet`.

    Centralises all ORM interactions related to pets.
    """

    def get_all(self) -> QuerySet:
        """Return all pets with their related owner pre-fetched."""
        return Pet.objects.select_related("owner").all()

    def get_by_id(self, pet_id: int) -> Pet:
        """Return the pet with the given primary key.

        Raises
        ------
        Pet.DoesNotExist
            If no pet with *pet_id* exists.
        """
        return Pet.objects.select_related("owner").get(pk=pet_id)

    def get_by_owner(self, owner: Owner) -> QuerySet:
        """Return all pets belonging to *owner*."""
        return Pet.objects.filter(owner=owner).select_related("owner")

    def save(self, pet: Pet) -> Pet:
        """Persist *pet* to the database and return the saved instance."""
        pet.save()
        return pet

    def delete(self, pet: Pet) -> None:
        """Delete *pet* from the database."""
        pet.delete()
