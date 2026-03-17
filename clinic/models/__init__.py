"""
Domain models for the PetClinic application.

This package exposes all core domain models:
- Owner: a pet owner with contact details
- Pet: a pet belonging to an owner
- Visit: a veterinary visit for a pet
- Doctor: a doctor registered in the clinic
"""

from clinic.models.owner import Owner
from clinic.models.pet import Pet
from clinic.models.visit import Visit
from clinic.models.doctor import Doctor

__all__ = ["Owner", "Pet", "Visit", "Doctor"]
