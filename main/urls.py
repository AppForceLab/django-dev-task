from django.urls import path

from .views import settings_view, translate_cv

urlpatterns = [
    path("settings/", settings_view, name="settings_view"),
    path("cv/<int:pk>/translate/", translate_cv, name="translate_cv"),
]
