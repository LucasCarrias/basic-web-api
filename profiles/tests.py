from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Profile
from posts.models import Post
from comments.models import Comment


class ProfileAPIReadTests(APITestCase):
    def setUp(self):
        for i in range(5):
            data = {
                'name': f'Test Profile {i}',
                'email': f'Test Email {i}'
            }
            profile_test = Profile(**data)
            profile_test.save()

    def test_list_profile(self):
        url = reverse('profile-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)
        self.assertEqual(response.data[0]['name'], 'Test Profile 0')

    def test_retrive_profile(self):
        url = reverse('profile-detail', kwargs={'pk':1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(response.data, None)
        self.assertEqual(response.data['name'], 'Test Profile 0')


class ProfileAPIInfoTests(APITestCase):
    def setUp(self):
        for n in range(2):
            profile_data = {
                'name': f'Test Profile {n}',
                'email': f'Test Email {n}'
            }
            profile_test = Profile(**profile_data)
            profile_test.save()
            
            for i in range(1, 6):
                post_data = {
                    'title': f'Test title {i}',
                    'body': f'Test body {i}',
                    'user': profile_test
                }
                post_test = Post(**post_data)
                post_test.save()

                for j in range(1, 7):
                    comment_data = {
                        'name': f'Test name {j}',
                        'body': f'Test body {j}',
                        'email': f'test{j}@email.com',
                        'post': post_test
                    }
                    comment_test = Comment(**comment_data)
                    comment_test.save()

    def test_profile_info(self):
        url = reverse('profile-info', kwargs={'pk':1})

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], 1)
        self.assertEqual(response.data['name'], 'Test Profile 0')
        self.assertEqual(response.data['total_posts'], 5)
        self.assertEqual(response.data['total_comments'], 30)