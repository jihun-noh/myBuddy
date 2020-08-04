from rest_framework import serializers
from .models import DivePoint, DiveLog, DiveCertOrg

class DivePointSerializer(serializers.ModelSerializer):
    class Meta:
        model = DivePoint
        fields = '__all__'

    def validate(self, data):
        if self.context['request'].method == 'POST':
            queryset = DivePoint.objects.filter(point_nm=data['point_nm'], diver=data['diver'])
            if queryset.exists():
                raise serializers.ValidationError('point_nm [{}] is already exist'.format(data['point_nm']))
        return data

class DiveLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiveLog
        fields = '__all__'

    def validate(self, data):
        if self.context['request'].method == 'POST':
            queryset = DiveLog.objects.filter(log_nm=data['log_nm'], diver=data['diver'])
            if queryset.exists():
                raise serializers.ValidationError('log_nm [{}] is already exist'.format(data['log_nm']))
        return data

class DiveCertOrgSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiveCertOrg
        fields = '__all__'
