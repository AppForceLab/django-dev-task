from rest_framework.test import APITestCase
from django.urls import reverse
from main.models import CV


class CVAPITestCase(APITestCase):
    def setUp(self):
        self.cv = CV.objects.create(
            firstname="John",
            lastname="Doe",
            bio="Backend Developer",
            skills="Python, Django, PostgreSQL",
            projects="Project Alpha",
            contacts="john@example.com",
        )
        self.list_url = reverse("api_v1_cv_list_create")
        self.detail_url = reverse("api_v1_cv_detail", args=[self.cv.pk])

    def test_list_cvs(self):
        """Should return list of CVs."""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_create_cv(self):
        """Should create a new CV."""
        data = {
            "firstname": "Jane",
            "lastname": "Smith",
            "bio": "Frontend dev",
            "skills": "React, TypeScript",
            "projects": "Site builder",
            "contacts": "jane@example.com",
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(CV.objects.count(), 2)

    def test_retrieve_cv(self):
        """Should retrieve CV by ID."""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["firstname"], self.cv.firstname)

    def test_update_cv(self):
        """Should update existing CV."""
        data = {
            "firstname": "Johnny",
            "lastname": "Doe",
            "bio": "Updated bio",
            "skills": "Python",
            "projects": "Updated project",
            "contacts": "john@example.com",
        }
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, 200)
        self.cv.refresh_from_db()
        self.assertEqual(self.cv.firstname, "Johnny")

    def test_delete_cv(self):
        """Should delete CV."""
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(CV.objects.count(), 0)
