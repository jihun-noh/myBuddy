from rest_framework import serializers
from .models import ObservationPost

class ObservationPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObservationPost
        fields = '__all__'
