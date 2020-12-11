"""Room Test Cases"""
import os
import requests
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

USER = get_user_model()


class RoomTestCase(APITestCase):
    """Room Test Cases"""

    def setUp(self):
        """
        Test Data Initialise method
        :return:
        """
        self.auth = requests.auth.HTTPBasicAuth("ankit", "Test@123")

        # Authenticate client with user
        self.data = {
            "name": "Test Room",
            "items": [1]
        }
        self.url = os.getenv('SITE_URL') + '/api/room/'

    def test_room_add(self):
        """
        Test Case to add room
        :return:
        """
        data = self.data.copy()
        response = requests.post(self.url, data=data, auth=self.auth)
        self.assertEqual(response.status_code, 201)

    def test_room_list(self):
        """
        Test Case to add room
        :return:
        """
        response = requests.get(self.url, auth=self.auth)
        self.assertEqual(response.status_code, 200)
