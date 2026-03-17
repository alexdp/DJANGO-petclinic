"""django-tables2 table definitions for the PetClinic application.

Each table class maps a model queryset to a sortable, paginated HTML table
that can be rendered in templates using the ``{% render_table %}`` tag.
"""

import django_tables2 as tables
from django.urls import reverse
from django.utils.html import format_html

from clinic.models import Owner, Pet, Visit
from clinic.models.doctor import Doctor


class OwnerTable(tables.Table):
    """Sortable table for :class:`~clinic.models.Owner` objects.

    A *detail* column renders a link to the owner's detail page.
    """

    detail = tables.Column(empty_values=(), orderable=False, verbose_name="")

    class Meta:
        model = Owner
        template_name = "django_tables2/bootstrap5.html"
        fields = ["first_name", "last_name", "email", "phone", "detail"]
        attrs = {"class": "table table-striped table-hover"}

    def render_detail(self, record: Owner) -> str:
        url = reverse("clinic:owner_detail", args=[record.pk])
        return format_html('<a href="{}" class="btn btn-sm btn-outline-primary">View</a>', url)

class DoctorTable(tables.Table):
    """Sortable table for :class:`~clinic.models.Doctor` objects.

    A *detail* column renders a link to the doctor's detail page.
    """

    detail = tables.Column(empty_values=(), orderable=False, verbose_name="")

    class Meta:
        model = Doctor
        template_name = "django_tables2/bootstrap5.html"
        fields = ["first_name", "last_name", "email", "phone", "detail"]
        attrs = {"class": "table table-striped table-hover"}

    def render_detail(self, record: Doctor) -> str:
        url = reverse("clinic:doctor_detail", args=[record.pk])
        return format_html('<a href="{}" class="btn btn-sm btn-outline-primary">View</a>', url)


class PetTable(tables.Table):
    """Sortable table for :class:`~clinic.models.Pet` objects."""

    owner = tables.Column(accessor="owner", verbose_name="Owner")

    class Meta:
        model = Pet
        template_name = "django_tables2/bootstrap5.html"
        fields = ["name", "type", "birth_date", "owner"]
        attrs = {"class": "table table-striped table-hover"}


class VisitTable(tables.Table):
    """Sortable table for :class:`~clinic.models.Visit` objects."""

    pet = tables.Column(accessor="pet", verbose_name="Pet")
    detail = tables.Column(empty_values=(), orderable=False, verbose_name="")

    class Meta:
        model = Visit
        template_name = "django_tables2/bootstrap5.html"
        fields = ["pet", "visit_date", "description", "detail"]
        attrs = {"class": "table table-striped table-hover"}

    def render_detail(self, record: Visit) -> str:
        url = reverse("clinic:visit_detail", args=[record.pk])
        return format_html('<a href="{}" class="btn btn-sm btn-outline-primary">View</a>', url)
