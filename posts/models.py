from django.db import models
from profiles.models import Profile


class Post(models.Model):
    title = models.CharField(max_length=127)
    body = models.TextField()
    user = models.ForeignKey(Profile, related_name='posts', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
