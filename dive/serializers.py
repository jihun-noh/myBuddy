from rest_framework import serializers
from .models import DivePoint, DiveLog

class DivePointSerializer(serializers.ModelSerializer):
    class Meta:
        model = DivePoint
        fields = '__all__'

class DiveLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiveLog
        fields = '__all__'
