from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Comment
from profiles.models import Profile
from posts.models import Post


class PostAPIReadTests(APITestCase):
    def setUp(self): 
        profile_data = {
            'name': 'Test Profile',
            'email': 'Test Email'
        }
        profile_test = Profile(**profile_data)
        profile_test.save()

        post_data = {
                'title': f'Test title',
                'body': f'Test body',
                'user': profile_test
            }
        post_test = Post(**post_data)
        post_test.save()
        
        for i in range(5):
            comment_data = {
                'name': f'Test name {i}',
                'body': f'Test body {i}',
                'email': f'test{i}@email.com',
                'post': post_test
            }
            comment_test = Comment(**comment_data)
            comment_test.save()

    def test_list_comment(self):
        url = reverse('comment-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)
        self.assertEqual(response.data[0]['name'], 'Test name 0')
        self.assertEqual(response.data[0]['postId'], '1')

    def test_retrieve_comment(self):
        url = reverse('comment-detail', kwargs={'pk':1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test name 0')
        self.assertEqual(response.data['postId'], '1')

