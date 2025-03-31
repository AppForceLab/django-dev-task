from django.db import models
from django.utils.timezone import now


class RequestLog(models.Model):
    timestamp = models.DateTimeField(default=now)
    method = models.CharField(max_length=10)
    path = models.CharField(max_length=200)
    query_string = models.TextField(blank=True)
    remote_ip = models.GenericIPAddressField(null=True, blank=True)
    user = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return f"{self.method} {self.path} [{self.timestamp:%Y-%m-%d %H:%M:%S}]"
