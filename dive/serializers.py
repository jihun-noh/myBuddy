from rest_framework import serializers
from .models import DivePoint, DiveLog

class DivePointSerializer(serializers.ModelSerializer):
    class Meta:
        model = DivePoint
        fields = '__all__'

    def validate(self, data):
         queryset = DivePoint.objects.filter(point_nm=data['point_nm'], diver=data['diver'])
         print(queryset)
         if queryset.exists():
             raise serializers.ValidationError('point_nm [{}] is already exist'.format(data['point_nm']))
         return data

class DiveLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiveLog
        fields = '__all__'
