from django.urls import path
from .views import request_log_list

urlpatterns = [
    path("logs/", request_log_list, name="request_log_list"),
]
