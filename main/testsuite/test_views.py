from django.test import TestCase
from django.urls import reverse
from main.models import CV

class CVViewsTest(TestCase):
    def setUp(self):
        self.cv = CV.objects.create(
            firstname="John",
            lastname="Doe",
            bio="Developer",
            skills="Python, Django",
            projects="Portfolio",
            contacts="john@example.com"
        )

    def test_cv_list_view(self):
        response = self.client.get(reverse("cv_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.cv.firstname)

    def test_cv_detail_view(self):
        response = self.client.get(reverse("cv_detail", args=[self.cv.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.cv.bio)
