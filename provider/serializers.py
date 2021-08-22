import json

from django.contrib.auth.models import User

from geojson import Polygon
from rest_framework import serializers

from provider.models import Provider
from provider.models import ServiceArea


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = '__all__'


class ServiceAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceArea
        fields = '__all__'

    def create(self, data):
        polygon = json.loads(data['polygon'])
        data['polygon'] = Polygon(*polygon['coordinates'])
        service_area = ServiceArea.objects.create(**data)
        return service_area
