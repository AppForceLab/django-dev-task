from django.urls import path, include

urlpatterns = [
    path("v1/", include("main.api.v1.urls")),
]
