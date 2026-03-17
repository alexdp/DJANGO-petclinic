"""Service responsible for doctor-related business logic."""

from django.db.models import QuerySet

from clinic.models import Owner
from clinic.models.doctor import Doctor
from clinic.repositories import OwnerRepo
from clinic.repositories.doctor_repo import DoctorRepo


class DoctorService:
    """Handles all use-cases that involve :class:`~clinic.models.Doctor`.

    Parameters
    ----------
    repo:
        An :class:`~clinic.repositories.DoctorRepo` instance.  Defaults to a
        fresh instance so callers do not need to inject one explicitly.
    """

    def __init__(self, repo: DoctorRepo | None = None) -> None:
        self.repo = repo or DoctorRepo()

    # ------------------------------------------------------------------
    # Queries
    # ------------------------------------------------------------------

    def list_doctors(self) -> QuerySet:
        """Return all doctors."""
        return self.repo.get_all()

    def get_doctor(self, doctor_id: int) -> Doctor:
        """Return the doctor identified by *doctor_id*."""
        return self.repo.get_by_id(doctor_id)

    # ------------------------------------------------------------------
    # Commands
    # ------------------------------------------------------------------

    def create_doctor(self, **kwargs) -> Doctor:
        """Create and persist a new doctor.

        Parameters
        ----------
        **kwargs:
            Field values accepted by :class:`~clinic.models.Doctor`.

        Returns
        -------
        Doctor
            The newly created doctor instance.
        """
        doctor = Doctor(**kwargs)
        return self.repo.save(doctor)

    def update_doctor(self, doctor: Doctor, **kwargs) -> Doctor:
        """Update *doctor* with the supplied field values and persist it.

        Parameters
        ----------
        doctor:
            The doctor instance to update.
        **kwargs:
            Field name/value pairs to apply.

        Returns
        -------
        Doctor
            The updated doctor instance.
        """
        for field, value in kwargs.items():
            setattr(doctor, field, value)
        return self.repo.save(doctor)

    def delete_doctor(self, doctor: Doctor) -> None:
        """Delete *doctor* from the system."""
        self.repo.delete(doctor)
