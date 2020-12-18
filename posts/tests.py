from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from profiles.models import Profile
from .models import Post


class PostAPIReadTests(APITestCase):
    def setUp(self): 
        profile_data = {
            'name': 'Test Profile',
            'email': 'Test Email'
        }
        profile_test = Profile(**profile_data)
        profile_test.save()
        
        for i in range(5):
            post_data = {
                'title': f'Test title {i}',
                'body': f'Test body {i}',
                'user': profile_test
            }
            post_test = Post(**post_data)
            post_test.save()

    def test_list_post(self):
        url = reverse('post-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)
        self.assertEqual(response.data[0]['title'], 'Test title 0')
        self.assertEqual(response.data[0]['userId'], '1')

    def test_retrieve_post(self):
        url = reverse('post-detail', kwargs={'pk':1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test title 0')
        self.assertEqual(response.data['userId'], '1')

