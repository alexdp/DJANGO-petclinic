"""Service responsible for owner-related business logic."""

from django.db.models import QuerySet

from clinic.models import Owner
from clinic.repositories import OwnerRepo


class OwnerService:
    """Handles all use-cases that involve :class:`~clinic.models.Owner`.

    Parameters
    ----------
    repo:
        An :class:`~clinic.repositories.OwnerRepo` instance.  Defaults to a
        fresh instance so callers do not need to inject one explicitly.
    """

    def __init__(self, repo: OwnerRepo | None = None) -> None:
        self.repo = repo or OwnerRepo()

    # ------------------------------------------------------------------
    # Queries
    # ------------------------------------------------------------------

    def list_owners(self) -> QuerySet:
        """Return all owners."""
        return self.repo.get_all()

    def get_owner(self, owner_id: int) -> Owner:
        """Return the owner identified by *owner_id*."""
        return self.repo.get_by_id(owner_id)

    # ------------------------------------------------------------------
    # Commands
    # ------------------------------------------------------------------

    def create_owner(self, **kwargs) -> Owner:
        """Create and persist a new owner.

        Parameters
        ----------
        **kwargs:
            Field values accepted by :class:`~clinic.models.Owner`.

        Returns
        -------
        Owner
            The newly created owner instance.
        """
        owner = Owner(**kwargs)
        return self.repo.save(owner)

    def update_owner(self, owner: Owner, **kwargs) -> Owner:
        """Update *owner* with the supplied field values and persist it.

        Parameters
        ----------
        owner:
            The owner instance to update.
        **kwargs:
            Field name/value pairs to apply.

        Returns
        -------
        Owner
            The updated owner instance.
        """
        for field, value in kwargs.items():
            setattr(owner, field, value)
        return self.repo.save(owner)

    def delete_owner(self, owner: Owner) -> None:
        """Delete *owner* from the system."""
        self.repo.delete(owner)
