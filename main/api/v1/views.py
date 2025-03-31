from rest_framework import generics
from main.models import CV
from .serializers import CVSerializer


class CVListCreateAPIView(generics.ListCreateAPIView):
    """
    get:
    List all CVs

    post:
    Create a new CV
    """

    queryset = CV.objects.all()
    serializer_class = CVSerializer


class CVRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    get:
    Retrieve a CV

    put:
    Update a CV

    delete:
    Delete a CV
    """

    queryset = CV.objects.all()
    serializer_class = CVSerializer
