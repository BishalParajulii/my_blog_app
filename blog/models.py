# models.py

from django.db import models
from django.contrib.auth.models import User

class PostModel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def total_likes(self):
        return self.likes.count() + self.anonymous_likes.count()

# class Like(models.Model):
#     post = models.ForeignKey(PostModel, related_name='likes', on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)

#     class Meta:
#         unique_together = ('post', 'user')

# class AnonymousLike(models.Model):
#     post = models.ForeignKey(PostModel, related_name='anonymous_likes', on_delete=models.CASCADE)
#     session_key = models.CharField(max_length=100)

#     class Meta:
#         unique_together = ('post', 'session_key')
