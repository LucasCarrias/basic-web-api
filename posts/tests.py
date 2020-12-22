from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from profiles.models import Profile
from comments.models import Comment
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

            for j in range(1, 6):
                comment_data = {
                    'name': f'Test name {j}',
                    'body': f'Test body {j}',
                    'email': f'test{j}@email.com',
                    'post': post_test
                }
                comment_test = Comment(**comment_data)
                comment_test.save()

    def test_list_post(self):
        url = reverse('post-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)
        self.assertEqual(response.data[0]['title'], 'Test title 0')
        self.assertEqual(response.data[0]['userId'], '1')

    def test_detail_post(self):
        url = reverse('post-detail', kwargs={'pk':1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test title 0')
        self.assertEqual(response.data['userId'], '1')

    def test_post_detail_comment_list(self):
        url = reverse('post-detail-comment-list', kwargs={'pk':1})

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)
        self.assertEqual(response.data[0]['name'], 'Test name 1')

    def test_post_detail_comment_detail(self):
        url = reverse('post-detail-comment-detail', kwargs={'post_pk':1, 'pk':2})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test name 2')


class PostCommentAPICRUDTests(APITestCase):
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

        comment_data = {
            'name': f'Test name 0',
            'body': f'Test body 0',
            'email': f'test@email.com',
            'post': post_test
        }
        comment_test = Comment(**comment_data)
        comment_test.save()
            

    def test_post_detail_comment_create(self):
        data = {
            'name': 'Test name',
            'email': 'test@test.com',
            'body': 'Test body'
        }
        url = reverse('post-detail-comment-list', kwargs={'pk':1})
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'Test name')

    def test_post_detail_comment_update(self):
        data = {
            'name': 'Test new name',
            'email': 'test@test.com',
            'body': 'Test body',
        }
        url = reverse('post-detail-comment-detail', kwargs={'post_pk':1, 'pk':1})
        response = self.client.put(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test new name')

    def test_post_detail_comment_patch(self):
        data = {
            'name': 'Test new name'
        }
        url = reverse('post-detail-comment-detail', kwargs={'post_pk':1, 'pk':1})
        response = self.client.patch(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test new name')

    def test_post_detail_comment_destroy(self):
        url = reverse('post-detail-comment-detail', kwargs={'post_pk':1, 'pk':1})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.data, None)
