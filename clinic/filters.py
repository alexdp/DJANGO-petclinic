"""django-filter FilterSet definitions for the PetClinic application.

Each FilterSet class provides a declarative way to filter querysets based on
URL query parameters supplied by the user.
"""

import django_filters

from clinic.models import Owner, Pet, Visit
from clinic.models.doctor import Doctor


class OwnerFilter(django_filters.FilterSet):
    """Filter owners by last name (case-insensitive, partial match)."""

    last_name = django_filters.CharFilter(
        lookup_expr="icontains",
        label="Last name",
    )

    class Meta:
        model = Owner
        fields = ["last_name"]


class DoctorFilter(django_filters.FilterSet):
    """Filter doctors by last name (case-insensitive, partial match)."""

    last_name = django_filters.CharFilter(
        lookup_expr="icontains",
        label="Last name",
    )

    class Meta:
        model = Doctor
        fields = ["last_name"]



class PetFilter(django_filters.FilterSet):
    """Filter pets by type and/or owner."""

    type = django_filters.CharFilter(
        lookup_expr="icontains",
        label="Type",
    )
    owner = django_filters.ModelChoiceFilter(
        queryset=Owner.objects.all(),
        label="Owner",
    )

    class Meta:
        model = Pet
        fields = ["type", "owner"]


class VisitFilter(django_filters.FilterSet):
    """Filter visits by visit date."""

    visit_date = django_filters.DateFilter(
        field_name="visit_date",
        label="Visit date",
    )

    class Meta:
        model = Visit
        fields = ["visit_date"]
