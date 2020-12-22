import json
from django.core.management.base import BaseCommand
from posts.serializers import PostSerializer
from comments.serializers import CommentSerializer
from profiles.serializers import ProfileSerializer


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        with open('./utils/mock_data.json') as file:
            data = json.load(file)
            users = data['users']
            posts = data['posts']
            comments = data['comments']
            
            self.stdout.write("Salvando dados de Profiles")
            save_profiles(users)
            self.stdout.write(f"{len(users)} profiles salvos com sucesso!")

            self.stdout.write("Salvando dados de Posts")
            save_posts(posts)
            self.stdout.write(f"{len(posts)} profiles salvos com sucesso!")

            self.stdout.write("Salvando dados de Comments")
            save_comments(comments)
            self.stdout.write(f"{len(comments)} profiles salvos com sucesso!")
        

def save_profiles(profiles):
    for profile in profiles:
        profile_serializer = ProfileSerializer(data=profile)
        
        if profile_serializer.is_valid(raise_exception=True):
            profile_serializer.save()

def save_posts(posts):
    for post in posts:
        post_serializer = PostSerializer(data=post)
        
        if post_serializer.is_valid(raise_exception=True):
            post_serializer.save()

def save_comments(comments):
    for comment in comments:
        comment_serializer = CommentSerializer(data=comment)
        
        if comment_serializer.is_valid(raise_exception=True):
            comment_serializer.save()