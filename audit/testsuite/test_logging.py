from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from audit.models import RequestLog


class RequestLoggingTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="tester", password="pass123")

    def test_logging_basic_request(self):
        """Middleware logs a basic GET request."""
        self.client.get("/")
        log = RequestLog.objects.last()
        self.assertIsNotNone(log)
        self.assertEqual(log.method, "GET")
        self.assertEqual(log.path, "/")

    def test_static_file_request_not_logged(self):
        """Middleware skips static file requests."""
        self.client.get("/static/css/style.css")
        self.assertEqual(RequestLog.objects.count(), 0)

    def test_logs_view_accessible(self):
        """The /logs/ view should return HTTP 200."""
        response = self.client.get("/logs/")
        self.assertEqual(response.status_code, 200)

    def test_authenticated_user_logged(self):
        """Middleware logs the username if user is authenticated."""
        self.client.login(username="tester", password="pass123")
        self.client.get("/cv/")
        log = RequestLog.objects.last()
        self.assertEqual(log.user, "tester")
