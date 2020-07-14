from rest_framework import serializers
from .models import ObservationPost

class ObservationPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObservationPost
        fields = '__all__'

    def to_internal_value(self, data):
        fixed_obs_lat = round(float(data.get('obs_lat')), 10)
        fixed_obs_lon = round(float(data.get('obs_lon')), 10)
        data.update({'obs_lat':fixed_obs_lat, 'obs_lon':fixed_obs_lon})
        return data
