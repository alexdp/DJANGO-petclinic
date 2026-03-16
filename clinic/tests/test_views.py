"""View integration tests using Django's test client."""

import datetime

from django.test import TestCase
from django.urls import reverse

from clinic.models import Owner, Pet, Visit


class OwnerViewTest(TestCase):
    """Tests for owner-related views."""

    def setUp(self):
        self.owner = Owner.objects.create(
            first_name="Nina",
            last_name="Ross",
            email="nina@example.com",
            phone="555-1400",
        )

    def test_owner_list_returns_200(self):
        response = self.client.get(reverse("clinic:owner_list"))
        self.assertEqual(response.status_code, 200)

    def test_owner_list_contains_owner_name(self):
        response = self.client.get(reverse("clinic:owner_list"))
        self.assertContains(response, "Nina")

    def test_owner_create_get_returns_200(self):
        response = self.client.get(reverse("clinic:owner_create"))
        self.assertEqual(response.status_code, 200)

    def test_owner_create_post_redirects(self):
        response = self.client.post(
            reverse("clinic:owner_create"),
            {
                "first_name": "Oliver",
                "last_name": "Stone",
                "email": "oliver@example.com",
                "phone": "555-1500",
            },
        )
        self.assertRedirects(response, reverse("clinic:owner_list"))
        self.assertTrue(Owner.objects.filter(email="oliver@example.com").exists())

    def test_owner_detail_returns_200(self):
        response = self.client.get(
            reverse("clinic:owner_detail", args=[self.owner.pk])
        )
        self.assertEqual(response.status_code, 200)

    def test_owner_detail_contains_name(self):
        response = self.client.get(
            reverse("clinic:owner_detail", args=[self.owner.pk])
        )
        self.assertContains(response, "Nina")

    def test_owner_list_filter_by_last_name(self):
        response = self.client.get(reverse("clinic:owner_list") + "?last_name=Ross")
        self.assertContains(response, "Nina")


class PetViewTest(TestCase):
    """Tests for pet-related views."""

    def setUp(self):
        self.owner = Owner.objects.create(
            first_name="Pat",
            last_name="Quinn",
            email="pat@example.com",
            phone="555-1600",
        )
        self.pet = Pet.objects.create(
            name="Rocky",
            birth_date=datetime.date(2020, 4, 1),
            type="dog",
            owner=self.owner,
        )

    def test_pet_list_returns_200(self):
        response = self.client.get(reverse("clinic:pet_list"))
        self.assertEqual(response.status_code, 200)

    def test_pet_list_contains_pet_name(self):
        response = self.client.get(reverse("clinic:pet_list"))
        self.assertContains(response, "Rocky")

    def test_pet_create_get_returns_200(self):
        response = self.client.get(reverse("clinic:pet_create"))
        self.assertEqual(response.status_code, 200)

    def test_pet_create_post_redirects(self):
        response = self.client.post(
            reverse("clinic:pet_create"),
            {
                "name": "Daisy",
                "birth_date": "2021-08-15",
                "type": "cat",
                "owner": self.owner.pk,
            },
        )
        self.assertRedirects(response, reverse("clinic:pet_list"))
        self.assertTrue(Pet.objects.filter(name="Daisy").exists())


class VisitViewTest(TestCase):
    """Tests for visit-related views."""

    def setUp(self):
        owner = Owner.objects.create(
            first_name="Rachel",
            last_name="Scott",
            email="rachel@example.com",
            phone="555-1700",
        )
        self.pet = Pet.objects.create(
            name="Biscuit",
            birth_date=datetime.date(2017, 12, 25),
            type="dog",
            owner=owner,
        )
        self.visit = Visit.objects.create(
            pet=self.pet,
            visit_date=datetime.date(2024, 2, 20),
            description="Flea treatment",
        )

    def test_visit_list_returns_200(self):
        response = self.client.get(reverse("clinic:visit_list"))
        self.assertEqual(response.status_code, 200)

    def test_visit_list_contains_description(self):
        response = self.client.get(reverse("clinic:visit_list"))
        self.assertContains(response, "Flea treatment")

    def test_visit_create_get_returns_200(self):
        response = self.client.get(reverse("clinic:visit_create"))
        self.assertEqual(response.status_code, 200)

    def test_visit_create_post_redirects(self):
        response = self.client.post(
            reverse("clinic:visit_create"),
            {
                "pet": self.pet.pk,
                "visit_date": "2024-09-01",
                "description": "Annual shots",
            },
        )
        self.assertRedirects(response, reverse("clinic:visit_list"))
        self.assertTrue(Visit.objects.filter(description="Annual shots").exists())
