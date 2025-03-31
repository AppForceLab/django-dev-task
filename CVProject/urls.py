from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from main import views

urlpatterns = [
    path("", views.cv_list, name="cv_list"),
    path("cv/<int:pk>/", views.cv_detail, name="cv_detail"),
    path("cv/<int:pk>/pdf/", views.download_cv_pdf, name="download_cv_pdf"),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path("api/", include("main.api.urls")),
]
