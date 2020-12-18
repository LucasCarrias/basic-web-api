from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from comments.models import Comment
from profiles.models import Profile
from posts.models import Post


class PostsCommentsAPIReadTests(APITestCase):
    def setUp(self):
        for i in range(1, 4):
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

                for k in range(1, 6):
                    comment_data = {
                        'name': f'Test name {i}',
                        'body': f'Test body {i}',
                        'email': f'test{i}@email.com',
                        'post': post_test
                    }
                    comment_test = Comment(**comment_data)
                    comment_test.save()
                

    def test_post_comments_list(self):
        url = reverse('post-comments-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 9)
        self.assertEqual(response.data[0]['title'], 'Test title 1')
        self.assertEqual(len(response.data[0]['comments']), 5)
        self.assertEqual(response.data[0]['comments'][0], 'http://testserver/comments/1')

    def test_post_comments_detail(self):
        url = reverse('post-comments-detail', kwargs={'pk':1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test title 1')
        self.assertEqual(len(response.data['comments']), 5)
        self.assertEqual(response.data['comments'][0], 'http://testserver/comments/1')