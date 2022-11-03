from rest_framework import serializers
from .models import IP_to_AWS_region_API

class IP_to_AWS_region_API_Serializer(serializers.ModelSerializer):
    class Meta:
        model = IP_to_AWS_region_API
        fields = ["ip"]