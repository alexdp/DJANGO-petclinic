"""ModelForms for creating and updating domain objects."""

from django import forms

from clinic.models import Owner, Pet, Visit


class OwnerForm(forms.ModelForm):
    """Form for creating / editing an :class:`~clinic.models.Owner`."""

    class Meta:
        model = Owner
        fields = ["first_name", "last_name", "email", "phone"]
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
        }


class PetForm(forms.ModelForm):
    """Form for creating / editing a :class:`~clinic.models.Pet`."""

    class Meta:
        model = Pet
        fields = ["name", "birth_date", "type", "owner"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "birth_date": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "type": forms.TextInput(attrs={"class": "form-control"}),
            "owner": forms.Select(attrs={"class": "form-select"}),
        }


class VisitForm(forms.ModelForm):
    """Form for creating / editing a :class:`~clinic.models.Visit`."""

    class Meta:
        model = Visit
        fields = ["pet", "visit_date", "description"]
        widgets = {
            "pet": forms.Select(attrs={"class": "form-select"}),
            "visit_date": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
        }
