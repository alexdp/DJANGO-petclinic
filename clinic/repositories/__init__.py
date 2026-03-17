"""
Repository layer for the PetClinic application.

The repository pattern isolates the data-access logic from the service/view
layers.  Each repository provides a stable CRUD interface so that the rest of
the application never accesses the ORM directly.
"""

from clinic.repositories.owner_repo import OwnerRepo
from clinic.repositories.pet_repo import PetRepo
from clinic.repositories.visit_repo import VisitRepo
from clinic.repositories.doctor_repo import DoctorRepo

__all__ = ["OwnerRepo", "PetRepo", "VisitRepo", "DoctorRepo"]
