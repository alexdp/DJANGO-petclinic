"""
Domain models for the PetClinic application.

This package exposes the three core domain models:
- Owner: a pet owner with contact details
- Pet: a pet belonging to an owner
- Visit: a veterinary visit for a pet
"""

from clinic.models.owner import Owner
from clinic.models.pet import Pet
from clinic.models.visit import Visit

__all__ = ["Owner", "Pet", "Visit"]
