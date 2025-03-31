from django.test import TestCase
from main.models import CV

class CVModelTest(TestCase):
    def test_str_method(self):
        cv = CV(firstname="Alice", lastname="Smith")
        self.assertEqual(str(cv), "Alice Smith")
