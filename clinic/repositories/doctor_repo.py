"""Repository for the Doctor aggregate."""

from django.db.models import QuerySet

from clinic.models import Doctor


class DoctorRepo:
    """Data-access object for :class:`~clinic.models.Doctor`.

    All database interactions for doctors are centralised here so that the
    service layer remains free of ORM specifics.
    """

    def get_all(self) -> QuerySet:
        """Return all doctors ordered by last name, first name."""
        return Doctor.objects.all()

    def get_by_id(self, doctor_id: int) -> Doctor:
        """Return the doctor with the given primary key.

        Raises
        ------
        Doctor.DoesNotExist
            If no doctor with *doctor_id* exists.
        """
        return Doctor.objects.get(pk=doctor_id)

    def save(self, doctor: Doctor) -> Doctor:
        """Persist *doctor* to the database and return the saved instance."""
        doctor.save()
        return doctor

    def delete(self, doctor: Doctor) -> None:
        """Delete *doctor* from the database."""
        doctor.delete()
