"""Views for the Owner entity.

Provides list, create, and detail views backed by OwnerService.
Tables are rendered via django-tables2 and filtered via django-filter.
"""

import django_tables2 as tables
from django.shortcuts import get_object_or_404, redirect, render

from clinic.filters import OwnerFilter
from clinic.forms import OwnerForm
from clinic.services import OwnerService
from clinic.tables import OwnerTable

_owner_service = OwnerService()


def owner_list_view(request):
    """Display a filterable, sortable, paginated list of all owners.

    GET parameters are used by :class:`~clinic.filters.OwnerFilter` to narrow
    the queryset before it is handed to :class:`~clinic.tables.OwnerTable`.
    """
    qs = _owner_service.list_owners()
    f = OwnerFilter(request.GET, queryset=qs)
    table = OwnerTable(f.qs)
    tables.RequestConfig(request, paginate={"per_page": 10}).configure(table)
    return render(
        request,
        "clinic/owner_list.html",
        {"filter": f, "table": table},
    )


def owner_create_view(request):
    """Display and process the owner creation form.

    On a valid POST the owner is persisted via :class:`~clinic.services.OwnerService`
    and the user is redirected to the owner list.
    """
    if request.method == "POST":
        form = OwnerForm(request.POST)
        if form.is_valid():
            _owner_service.create_owner(**form.cleaned_data)
            return redirect("clinic:owner_list")
    else:
        form = OwnerForm()
    return render(request, "clinic/owner_create.html", {"form": form})


def owner_detail_view(request, owner_id: int):
    """Display the detail page for a single owner.

    Also lists the owner's pets and, on POST, handles owner updates.
    """
    from clinic.services import PetService
    from clinic.tables import PetTable

    owner = get_object_or_404(_owner_service.list_owners(), pk=owner_id)

    if request.method == "POST":
        form = OwnerForm(request.POST, instance=owner)
        if form.is_valid():
            form.save()
            return redirect("clinic:owner_detail", owner_id=owner.pk)
    else:
        form = OwnerForm(instance=owner)

    pet_service = PetService()
    pets_qs = pet_service.find_pets_by_owner(owner)
    pet_table = PetTable(pets_qs)
    tables.RequestConfig(request, paginate={"per_page": 10}).configure(pet_table)

    return render(
        request,
        "clinic/owner_detail.html",
        {"owner": owner, "form": form, "pet_table": pet_table},
    )
