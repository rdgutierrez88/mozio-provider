import json

from rest_framework.test import APIClient
from rest_framework.test import APITestCase


class Test(APITestCase):
    client = APIClient()

    url = 'http://127.0.0.1:8000/'
    providers = 'providers/'
    service_areas = 'service_areas/'

    provider1 = {
        'name': 'test',
        'email': 'test@test.com',
        'number': '+6391234567',
        'language': 'ph',
        'currency': 'php'
    }

    provider2 = {
        'name': 'jt express',
        'email': 'test@test.com',
        'number': '+6391234567',
        'language': 'ph',
        'currency': 'php'
    }

    service_area1 = {
        'name': '1',
        'price': '1.00',
        'polygon': '{"type": "Polygon", "coordinates": [[[35.0, 10.0], [45.0, 45.0], [15.0, 40.0], [10.0, 20.0], [35.0, 10.0]]]}',
        'provider': 1
    }

    service_area2 = {
        'name': 'square',
        'price': '2.00',
        'polygon': '{"type": "Polygon", "coordinates": [[[100.0, 0.0], [101.0, 0.0], [101.0, 1.0], [100.0, 1.0], [100.0, 0.0]]]}',
        'provider': 1
    }

    point = '?lat=70&lng=70'

    def test_create_provider(self):
        response = self.client.post(self.url + self.providers, self.provider1)
        self.assertEqual(201, response.status_code)

    def test_create_service_area(self):
        response = self.client.post(self.url + self.providers, self.provider1)
        response = self.client.post(self.url + self.service_areas, self.service_area1)
        self.assertEqual(201, response.status_code)

    def test_read_provider(self):
        response = self.client.post(self.url + self.providers, self.provider1)
        response = self.client.get(self.url + self.providers)
        self.assertEqual(200, response.status_code)

    def test_read_service_area(self):
        response = self.client.post(self.url + self.providers, self.provider1)
        response = self.client.post(self.url + self.service_areas, self.service_area1)
        response = self.client.get(self.url + self.service_areas)
        self.assertEqual(200, response.status_code)

    def test_update_provider(self):
        response = self.client.post(self.url + self.providers, self.provider1)
        response = self.client.put(self.url + self.providers + '1/', self.provider2)
        response_data = json.loads(response.content)
        self.assertEqual(response_data.get("name"), self.provider2.get("name"))

    def test_update_service_area(self):
        response = self.client.post(self.url + self.providers, self.provider1)
        response = self.client.post(self.url + self.service_areas, self.service_area1)
        response = self.client.put(self.url + self.service_areas + '1/', self.service_area2)
        response_data = json.loads(response.content)
        self.assertEqual(response_data.get("name"), self.service_area2.get("name"))

    def test_delete_provider(self):
        response = self.client.post(self.url + self.providers, self.provider1)
        response = self.client.delete(self.url + self.providers + "1/")
        self.assertEqual(204, response.status_code)

    def test_delete_service_area(self):
        response = self.client.post(self.url + self.providers, self.provider1)
        response = self.client.post(self.url + self.service_areas, self.service_area1)
        response = self.client.delete(self.url + self.service_areas + "1/")
        self.assertEqual(204, response.status_code)

    def test_pip_test(self):
        response = self.client.post(self.url + self.providers, self.provider1)
        response = self.client.post(self.url + self.service_areas, self.service_area1)
        response = self.client.post(self.url + self.service_areas, self.service_area2)
        response = self.client.get(self.url + self.service_areas + self.point)
        response_data = json.loads(response.content)
        self.assertEqual(0, response_data.get('count'))

        response = self.client.put(self.url + self.service_areas + '1/', self.service_area2)
        response = self.client.get(self.url + self.service_areas + self.point)
        response_data = json.loads(response.content)
        self.assertEqual(1, response_data.get('count'))

