"""Tests for the service layer."""

import datetime

from django.test import TestCase

from clinic.models import Owner, Pet, Visit
from clinic.services import OwnerService, PetService, VisitService


class OwnerServiceTest(TestCase):
    """Tests for OwnerService."""

    def setUp(self):
        self.service = OwnerService()

    def test_create_owner(self):
        owner = self.service.create_owner(
            first_name="Hannah",
            last_name="Lee",
            email="hannah@example.com",
            phone="555-0800",
        )
        self.assertIsNotNone(owner.pk)
        self.assertEqual(owner.last_name, "Lee")

    def test_list_owners(self):
        self.service.create_owner(
            first_name="Ivan",
            last_name="Martin",
            email="ivan@example.com",
            phone="555-0900",
        )
        owners = self.service.list_owners()
        self.assertGreaterEqual(owners.count(), 1)

    def test_update_owner(self):
        owner = self.service.create_owner(
            first_name="Jane",
            last_name="Doe",
            email="jane@example.com",
            phone="555-1000",
        )
        updated = self.service.update_owner(owner, phone="555-9999")
        self.assertEqual(updated.phone, "555-9999")

    def test_delete_owner(self):
        owner = self.service.create_owner(
            first_name="Karl",
            last_name="Müller",
            email="karl@example.com",
            phone="555-1100",
        )
        pk = owner.pk
        self.service.delete_owner(owner)
        self.assertFalse(Owner.objects.filter(pk=pk).exists())


class PetServiceTest(TestCase):
    """Tests for PetService."""

    def setUp(self):
        self.service = PetService()
        self.owner = Owner.objects.create(
            first_name="Laura",
            last_name="Novak",
            email="laura@example.com",
            phone="555-1200",
        )

    def test_create_pet(self):
        pet = self.service.create_pet(
            name="Max",
            birth_date=datetime.date(2022, 7, 4),
            type="dog",
            owner=self.owner,
        )
        self.assertIsNotNone(pet.pk)

    def test_list_pets(self):
        self.service.create_pet(
            name="Mia",
            birth_date=datetime.date(2021, 11, 11),
            type="cat",
            owner=self.owner,
        )
        pets = self.service.list_pets()
        self.assertGreaterEqual(pets.count(), 1)

    def test_find_pets_by_owner(self):
        pet = self.service.create_pet(
            name="Oscar",
            birth_date=datetime.date(2020, 3, 3),
            type="rabbit",
            owner=self.owner,
        )
        pets = self.service.find_pets_by_owner(self.owner)
        self.assertIn(pet, pets)


class VisitServiceTest(TestCase):
    """Tests for VisitService."""

    def setUp(self):
        self.service = VisitService()
        owner = Owner.objects.create(
            first_name="Mike",
            last_name="Park",
            email="mike@example.com",
            phone="555-1300",
        )
        self.pet = Pet.objects.create(
            name="Peanut",
            birth_date=datetime.date(2019, 2, 14),
            type="hamster",
            owner=owner,
        )

    def test_create_visit(self):
        visit = self.service.create_visit(
            pet=self.pet,
            visit_date=datetime.date(2024, 6, 1),
            description="Health check",
        )
        self.assertIsNotNone(visit.pk)

    def test_list_visits(self):
        self.service.create_visit(
            pet=self.pet,
            visit_date=datetime.date(2024, 7, 1),
            description="Teeth cleaning",
        )
        visits = self.service.list_visits()
        self.assertGreaterEqual(visits.count(), 1)

    def test_list_visits_for_pet(self):
        visit = self.service.create_visit(
            pet=self.pet,
            visit_date=datetime.date(2024, 8, 1),
            description="Nail trim",
        )
        visits = self.service.list_visits_for_pet(self.pet)
        self.assertIn(visit, visits)
