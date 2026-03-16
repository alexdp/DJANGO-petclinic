"""Tests for domain models (Owner, Pet, Visit)."""

import datetime

from django.test import TestCase

from clinic.models import Owner, Pet, Visit


class OwnerModelTest(TestCase):
    """Tests for the Owner model."""

    def setUp(self):
        self.owner = Owner.objects.create(
            first_name="Alice",
            last_name="Smith",
            email="alice@example.com",
            phone="555-0100",
        )

    def test_str(self):
        self.assertEqual(str(self.owner), "Alice Smith")

    def test_fields_stored(self):
        owner = Owner.objects.get(pk=self.owner.pk)
        self.assertEqual(owner.first_name, "Alice")
        self.assertEqual(owner.last_name, "Smith")
        self.assertEqual(owner.email, "alice@example.com")
        self.assertEqual(owner.phone, "555-0100")


class PetModelTest(TestCase):
    """Tests for the Pet model."""

    def setUp(self):
        self.owner = Owner.objects.create(
            first_name="Bob",
            last_name="Jones",
            email="bob@example.com",
            phone="555-0200",
        )
        self.pet = Pet.objects.create(
            name="Rex",
            birth_date=datetime.date(2020, 1, 15),
            type="dog",
            owner=self.owner,
        )

    def test_str(self):
        self.assertEqual(str(self.pet), "Rex (dog)")

    def test_owner_relation(self):
        self.assertEqual(self.pet.owner, self.owner)


class VisitModelTest(TestCase):
    """Tests for the Visit model."""

    def setUp(self):
        owner = Owner.objects.create(
            first_name="Carol",
            last_name="White",
            email="carol@example.com",
            phone="555-0300",
        )
        pet = Pet.objects.create(
            name="Whiskers",
            birth_date=datetime.date(2019, 6, 1),
            type="cat",
            owner=owner,
        )
        self.visit = Visit.objects.create(
            pet=pet,
            visit_date=datetime.date(2024, 3, 10),
            description="Annual check-up",
        )

    def test_str(self):
        self.assertIn("Whiskers", str(self.visit))
        self.assertIn("2024-03-10", str(self.visit))

    def test_pet_relation(self):
        self.assertEqual(self.visit.pet.name, "Whiskers")
