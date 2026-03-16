"""Views for the Pet entity.

Provides list and create views backed by PetService.
"""

import django_tables2 as tables
from django.shortcuts import redirect, render

from clinic.filters import PetFilter
from clinic.forms import PetForm
from clinic.services import PetService
from clinic.tables import PetTable

_pet_service = PetService()


def pet_list_view(request):
    """Display a filterable, sortable, paginated list of all pets.

    GET parameters are used by :class:`~clinic.filters.PetFilter` to narrow
    the queryset.
    """
    qs = _pet_service.list_pets()
    f = PetFilter(request.GET, queryset=qs)
    table = PetTable(f.qs)
    tables.RequestConfig(request, paginate={"per_page": 10}).configure(table)
    return render(
        request,
        "clinic/pet_list.html",
        {"filter": f, "table": table},
    )


def pet_create_view(request):
    """Display and process the pet creation form.

    On a valid POST the pet is persisted via :class:`~clinic.services.PetService`
    and the user is redirected to the pet list.
    """
    if request.method == "POST":
        form = PetForm(request.POST)
        if form.is_valid():
            _pet_service.create_pet(**form.cleaned_data)
            return redirect("clinic:pet_list")
    else:
        form = PetForm()
    return render(request, "clinic/pet_create.html", {"form": form})
