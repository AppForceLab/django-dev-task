from rest_framework import serializers
from main.models import CV


class CVSerializer(serializers.ModelSerializer):
    """Serializer for CV with basic validation."""

    firstname = serializers.CharField(min_length=2)
    lastname = serializers.CharField(min_length=2)
    contacts = serializers.EmailField()

    class Meta:
        model = CV
        fields = "__all__"
