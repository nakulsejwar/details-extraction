from rest_framework import serializers
from .models import Aadhar

class AadharSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aadhar
        fields = ['aadhar_number']  # Only include Aadhar number
