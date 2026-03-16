"""Tests for the repository layer."""

import datetime

from django.test import TestCase

from clinic.models import Owner, Pet, Visit
from clinic.repositories import OwnerRepo, PetRepo, VisitRepo


class OwnerRepoTest(TestCase):
    """Tests for OwnerRepo."""

    def setUp(self):
        self.repo = OwnerRepo()
        self.owner = Owner.objects.create(
            first_name="Dave",
            last_name="Brown",
            email="dave@example.com",
            phone="555-0400",
        )

    def test_get_all(self):
        qs = self.repo.get_all()
        self.assertIn(self.owner, qs)

    def test_get_by_id(self):
        result = self.repo.get_by_id(self.owner.pk)
        self.assertEqual(result, self.owner)

    def test_save_creates(self):
        new_owner = Owner(
            first_name="Eve",
            last_name="Green",
            email="eve@example.com",
            phone="555-0500",
        )
        saved = self.repo.save(new_owner)
        self.assertIsNotNone(saved.pk)

    def test_delete(self):
        pk = self.owner.pk
        self.repo.delete(self.owner)
        self.assertFalse(Owner.objects.filter(pk=pk).exists())


class PetRepoTest(TestCase):
    """Tests for PetRepo."""

    def setUp(self):
        self.repo = PetRepo()
        self.owner = Owner.objects.create(
            first_name="Frank",
            last_name="Hall",
            email="frank@example.com",
            phone="555-0600",
        )
        self.pet = Pet.objects.create(
            name="Buddy",
            birth_date=datetime.date(2021, 5, 20),
            type="dog",
            owner=self.owner,
        )

    def test_get_all(self):
        qs = self.repo.get_all()
        self.assertIn(self.pet, qs)

    def test_get_by_id(self):
        result = self.repo.get_by_id(self.pet.pk)
        self.assertEqual(result, self.pet)

    def test_get_by_owner(self):
        qs = self.repo.get_by_owner(self.owner)
        self.assertIn(self.pet, qs)

    def test_delete(self):
        pk = self.pet.pk
        self.repo.delete(self.pet)
        self.assertFalse(Pet.objects.filter(pk=pk).exists())


class VisitRepoTest(TestCase):
    """Tests for VisitRepo."""

    def setUp(self):
        self.repo = VisitRepo()
        owner = Owner.objects.create(
            first_name="Grace",
            last_name="King",
            email="grace@example.com",
            phone="555-0700",
        )
        self.pet = Pet.objects.create(
            name="Luna",
            birth_date=datetime.date(2018, 9, 12),
            type="cat",
            owner=owner,
        )
        self.visit = Visit.objects.create(
            pet=self.pet,
            visit_date=datetime.date(2024, 1, 5),
            description="Vaccination",
        )

    def test_get_all(self):
        qs = self.repo.get_all()
        self.assertIn(self.visit, qs)

    def test_get_by_id(self):
        result = self.repo.get_by_id(self.visit.pk)
        self.assertEqual(result, self.visit)

    def test_get_by_pet(self):
        qs = self.repo.get_by_pet(self.pet)
        self.assertIn(self.visit, qs)

    def test_delete(self):
        pk = self.visit.pk
        self.repo.delete(self.visit)
        self.assertFalse(Visit.objects.filter(pk=pk).exists())
