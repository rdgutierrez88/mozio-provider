from rest_framework import viewsets
from rest_framework import permissions

from provider.models import Provider
from provider.models import ServiceArea

from provider.serializers import ProviderSerializer
from provider.serializers import ServiceAreaSerializer


class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all().order_by('name')
    serializer_class = ProviderSerializer
    permission_classes = [permissions.AllowAny]


class ServiceAreaViewSet(viewsets.ModelViewSet):
    queryset = ServiceArea.objects.all().order_by('name')
    serializer_class = ServiceAreaSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        lat = self.request.query_params.get('lat', None)
        lng = self.request.query_params.get('lng', None)

        queryset = ServiceArea.objects.all().order_by('name')
        if lat and lng and queryset.exists():
            lat = int(lat)
            lng = int(lng)
            service_areas = []
            for service_area in queryset:
                if service_area.contains(lat, lng):
                   service_areas.append(service_area.id)

            queryset = ServiceArea.objects.filter(id__in=service_areas).order_by('name')

        return queryset