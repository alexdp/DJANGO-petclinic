"""
Views package for the PetClinic application.

Views are organised by domain entity (owner, pet, visit) and imported here
for a flat, convenient access path.
"""

from clinic.views.owner_views import owner_create_view, owner_detail_view, owner_list_view
from clinic.views.pet_views import pet_create_view, pet_list_view
from clinic.views.visit_views import visit_create_view, visit_list_view

__all__ = [
    "owner_list_view",
    "owner_create_view",
    "owner_detail_view",
    "pet_list_view",
    "pet_create_view",
    "visit_list_view",
    "visit_create_view",
]
