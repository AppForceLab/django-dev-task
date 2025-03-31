from django.urls import path
from .views import CVListCreateAPIView, CVRetrieveUpdateDestroyAPIView

urlpatterns = [
    path("cv/", CVListCreateAPIView.as_view(), name="api_v1_cv_list_create"),
    path(
        "cv/<int:pk>/",
        CVRetrieveUpdateDestroyAPIView.as_view(),
        name="api_v1_cv_detail",
    ),
]
