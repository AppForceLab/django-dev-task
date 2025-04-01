from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from main import views


urlpatterns = [
    path("admin/", admin.site.urls),
    # Web views
    path("", views.cv_list, name="cv_list"),
    path("cv/<int:pk>/", views.cv_detail, name="cv_detail"),
    path("cv/<int:pk>/pdf/", views.download_cv_pdf, name="download_cv_pdf"),
    # Include subroutes
    path("", include("main.urls")),
    path("", include("audit.urls")),
    # API
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path("api/", include("main.api.urls")),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
