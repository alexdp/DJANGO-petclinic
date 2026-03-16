"""Django admin configuration for the PetClinic application.

All three domain models are registered with appropriate list_display,
list_filter, and search_fields to make the admin site immediately useful.
"""

from django.contrib import admin

from clinic.models import Owner, Pet, Visit


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    """Admin configuration for :class:`~clinic.models.Owner`."""

    list_display = ["first_name", "last_name", "email", "phone"]
    list_filter = ["last_name"]
    search_fields = ["first_name", "last_name", "email", "phone"]


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    """Admin configuration for :class:`~clinic.models.Pet`."""

    list_display = ["name", "type", "birth_date", "owner"]
    list_filter = ["type"]
    search_fields = ["name", "type", "owner__first_name", "owner__last_name"]


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    """Admin configuration for :class:`~clinic.models.Visit`."""

    list_display = ["pet", "visit_date", "description"]
    list_filter = ["visit_date"]
    search_fields = ["pet__name", "description"]
