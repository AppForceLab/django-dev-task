from django.urls import path

from main import views

urlpatterns = [
    path("", views.cv_list, name="cv_list"),
    path("cv/<int:pk>/", views.cv_detail, name="cv_detail"),
    path("cv/<int:pk>/pdf/", views.download_cv_pdf, name="download_cv_pdf"),
]
