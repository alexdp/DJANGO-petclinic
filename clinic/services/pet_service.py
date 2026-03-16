"""Service responsible for pet-related business logic."""

from django.db.models import QuerySet

from clinic.models import Owner, Pet
from clinic.repositories import PetRepo


class PetService:
    """Handles all use-cases that involve :class:`~clinic.models.Pet`.

    Parameters
    ----------
    repo:
        A :class:`~clinic.repositories.PetRepo` instance.
    """

    def __init__(self, repo: PetRepo | None = None) -> None:
        self.repo = repo or PetRepo()

    # ------------------------------------------------------------------
    # Queries
    # ------------------------------------------------------------------

    def list_pets(self) -> QuerySet:
        """Return all pets."""
        return self.repo.get_all()

    def get_pet(self, pet_id: int) -> Pet:
        """Return the pet identified by *pet_id*."""
        return self.repo.get_by_id(pet_id)

    def find_pets_by_owner(self, owner: Owner) -> QuerySet:
        """Return all pets that belong to *owner*."""
        return self.repo.get_by_owner(owner)

    # ------------------------------------------------------------------
    # Commands
    # ------------------------------------------------------------------

    def create_pet(self, **kwargs) -> Pet:
        """Create and persist a new pet.

        Parameters
        ----------
        **kwargs:
            Field values accepted by :class:`~clinic.models.Pet`.

        Returns
        -------
        Pet
            The newly created pet instance.
        """
        pet = Pet(**kwargs)
        return self.repo.save(pet)

    def delete_pet(self, pet: Pet) -> None:
        """Delete *pet* from the system."""
        self.repo.delete(pet)
