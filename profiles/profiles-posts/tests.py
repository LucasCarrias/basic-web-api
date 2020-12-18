from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from profiles.models import Profile
from posts.models import Post


class ProfilePostsAPIReadTests(APITestCase):
    def setUp(self):
        for i in range(1, 6):
            profile_data = {
                'name': f'Test Profile {i}',
                'email': f'Test Email {i}'
            }
            profile_test = Profile(**profile_data)
            profile_test.save()

            for j in range(1, 4):
                post_data = {
                    'title': f'Test title {j}',
                    'body': f'Test body {j}',
                    'user': profile_test
                }

                post_test = Post(**post_data)
                post_test.save()
                

    def test_profile_post_list(self):
        url = reverse('profile-posts-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)
        self.assertEqual(response.data[0]['name'], 'Test Profile 1')
        self.assertEqual(len(response.data[0]['posts']), 3)
        self.assertEqual(response.data[0]['posts'][0], 'http://testserver/posts/1')

    def test_profile_post_detail(self):
        url = reverse('profile-posts-detail', kwargs={'pk':1})

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Profile 1')
        self.assertEqual(len(response.data['posts']), 3)
        self.assertEqual(response.data['posts'][0], 'http://testserver/posts/1')