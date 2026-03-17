"""Views for the Visit entity.

Provides list and create views backed by VisitService.
"""

import django_tables2 as tables
from django.shortcuts import get_object_or_404, redirect, render

from clinic.filters import VisitFilter
from clinic.forms import VisitForm
from clinic.services import VisitService
from clinic.tables import VisitTable

_visit_service = VisitService()


def visit_list_view(request):
    """Display a filterable, sortable, paginated list of all visits.

    GET parameters are used by :class:`~clinic.filters.VisitFilter` to narrow
    the queryset.
    """
    qs = _visit_service.list_visits()
    f = VisitFilter(request.GET, queryset=qs)
    table = VisitTable(f.qs)
    tables.RequestConfig(request, paginate={"per_page": 10}).configure(table)
    return render(
        request,
        "clinic/visit_list.html",
        {"filter": f, "table": table},
    )


def visit_create_view(request):
    """Display and process the visit creation form.

    On a valid POST the visit is persisted via :class:`~clinic.services.VisitService`
    and the user is redirected to the visit list.
    """
    if request.method == "POST":
        form = VisitForm(request.POST)
        if form.is_valid():
            _visit_service.create_visit(**form.cleaned_data)
            return redirect("clinic:visit_list")
    else:
        form = VisitForm()
    return render(request, "clinic/visit_create.html", {"form": form})

def visit_detail_view(request, visit_id: int):
    """Display the detail page for a single visit.

    On POST, updates the visit and redirects back to this page.
    """
    visit = get_object_or_404(_visit_service.list_visits(), pk=visit_id)

    if request.method == "POST":
        form = VisitForm(request.POST, instance=visit)
        if form.is_valid():
            form.save()
            return redirect("clinic:visit_detail", visit_id=visit.pk)
    else:
        form = VisitForm(instance=visit)


    return render(
        request,
        "clinic/visit_detail.html",
        {"visit": visit, "form": form},
    )
