from django.db import models
from posts.models import Post


class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.name} at {post.title}"