"""
Service layer for the PetClinic application.

Services encapsulate business logic and orchestrate repository calls.
Views should only interact with this layer, never with repositories or the ORM
directly.
"""

from clinic.services.owner_service import OwnerService
from clinic.services.pet_service import PetService
from clinic.services.visit_service import VisitService

__all__ = ["OwnerService", "PetService", "VisitService"]
