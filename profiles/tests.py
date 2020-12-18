from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Profile


class ProfileAPIReadTests(APITestCase):
    def setUp(self):
        data = {
            'name': 'Test Profile',
            'email': 'Test Email'
        }
        profile_test = Profile(**data)
        profile_test.save()

    def test_list_profile(self):
        url = reverse('profile-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Test Profile')

    def test_retrive_profile(self):
        url = reverse('profile-detail', kwargs={'pk':1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(response.data, None)
        self.assertEqual(response.data['name'], 'Test Profile')
        

    # def test_list_profile_posts_list(self):
    #     url = reverse('profile-post-list')