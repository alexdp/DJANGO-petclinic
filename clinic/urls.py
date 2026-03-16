"""URL configuration for the clinic application.

Routes:
    /owners/              – owner list
    /owners/create/       – create a new owner
    /owners/<id>/         – owner detail / edit
    /pets/                – pet list
    /pets/create/         – create a new pet
    /visits/              – visit list
    /visits/create/       – create a new visit
"""

from django.urls import path

from clinic import views

app_name = "clinic"

urlpatterns = [
    # Owner routes
    path("owners/", views.owner_list_view, name="owner_list"),
    path("owners/create/", views.owner_create_view, name="owner_create"),
    path("owners/<int:owner_id>/", views.owner_detail_view, name="owner_detail"),
    # Pet routes
    path("pets/", views.pet_list_view, name="pet_list"),
    path("pets/create/", views.pet_create_view, name="pet_create"),
    # Visit routes
    path("visits/", views.visit_list_view, name="visit_list"),
    path("visits/create/", views.visit_create_view, name="visit_create"),
]
