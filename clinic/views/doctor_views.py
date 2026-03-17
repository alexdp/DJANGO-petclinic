"""Views for the Doctor entity.

Provides list, create, and detail views backed by DoctorService.
Tables are rendered via django-tables2 and filtered via django-filter.
"""

import django_tables2 as tables
from django.shortcuts import get_object_or_404, redirect, render

from clinic.filters import DoctorFilter
from clinic.forms import DoctorForm
from clinic.services import DoctorService
from clinic.services.visit_service import VisitService
from clinic.tables import DoctorTable, VisitTable

_doctor_service = DoctorService()


def doctor_list_view(request):
    """Display a filterable, sortable, paginated list of all doctors.

    GET parameters are used by :class:`~clinic.filters.DoctorFilter` to narrow
    the queryset before it is handed to :class:`~clinic.tables.DoctorTable`.
    """
    qs = _doctor_service.list_doctors()
    f = DoctorFilter(request.GET, queryset=qs)
    table = DoctorTable(f.qs)
    tables.RequestConfig(request, paginate={"per_page": 10}).configure(table)
    return render(
        request,
        "clinic/doctor_list.html",
        {"filter": f, "table": table},
    )


def doctor_create_view(request):
    """Display and process the doctor creation form.

    On a valid POST the doctor is persisted via :class:`~clinic.services.DoctorService`
    and the user is redirected to the doctor list.
    """
    if request.method == "POST":
        form = DoctorForm(request.POST)
        if form.is_valid():
            _doctor_service.create_doctor(**form.cleaned_data)
            return redirect("clinic:doctor_list")
    else:
        form = DoctorForm()
    return render(request, "clinic/doctor_create.html", {"form": form})


def doctor_detail_view(request, doctor_id: int):
    """Display the detail page for a single doctor.

    Also lists the doctor's appointments and, on POST, handles doctor updates.
    """
    from clinic.services import PetService
    from clinic.tables import PetTable

    doctor = get_object_or_404(_doctor_service.list_doctors(), pk=doctor_id)

    if request.method == "POST":
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect("clinic:doctor_detail", doctor_id=doctor.pk)
    else:
        form = DoctorForm(instance=doctor)

    visit_service = VisitService()
    visits_qs = visit_service.list_visits_for_doctor(doctor)
    visit_table = VisitTable(visits_qs)
    tables.RequestConfig(request, paginate={"per_page": 10}).configure(visit_table)


    return render(
        request,
        "clinic/doctor_detail.html",
        {"doctor": doctor, "form": form, "visit_table": visit_table},
    )
