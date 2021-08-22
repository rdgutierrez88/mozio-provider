from django.db import models

from djgeojson.fields import PolygonField

from shapely.geometry import shape
from shapely.geometry import Point
from shapely.geometry import Polygon


class Provider(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    number = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    currency = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ServiceArea(models.Model):
    provider = models.ForeignKey(Provider, related_name="service_area", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    polygon = PolygonField()

    def __str__(self):
        return self.name

    @property
    def provider_name(self):
        return self.provider.name

    def contains(self, lat, lng):
        point = Point(lat, lng)
        polygon = shape(self.polygon)
        return polygon.contains(point)