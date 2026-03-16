"""Service responsible for visit-related business logic."""

from django.db.models import QuerySet

from clinic.models import Pet, Visit
from clinic.repositories import VisitRepo


class VisitService:
    """Handles all use-cases that involve :class:`~clinic.models.Visit`.

    Parameters
    ----------
    repo:
        A :class:`~clinic.repositories.VisitRepo` instance.
    """

    def __init__(self, repo: VisitRepo | None = None) -> None:
        self.repo = repo or VisitRepo()

    # ------------------------------------------------------------------
    # Queries
    # ------------------------------------------------------------------

    def list_visits(self) -> QuerySet:
        """Return all visits."""
        return self.repo.get_all()

    def list_visits_for_pet(self, pet: Pet) -> QuerySet:
        """Return all visits for *pet*, most recent first."""
        return self.repo.get_by_pet(pet)

    def get_visit(self, visit_id: int) -> Visit:
        """Return the visit identified by *visit_id*."""
        return self.repo.get_by_id(visit_id)

    # ------------------------------------------------------------------
    # Commands
    # ------------------------------------------------------------------

    def create_visit(self, **kwargs) -> Visit:
        """Create and persist a new visit.

        Parameters
        ----------
        **kwargs:
            Field values accepted by :class:`~clinic.models.Visit`.

        Returns
        -------
        Visit
            The newly created visit instance.
        """
        visit = Visit(**kwargs)
        return self.repo.save(visit)

    def delete_visit(self, visit: Visit) -> None:
        """Delete *visit* from the system."""
        self.repo.delete(visit)
