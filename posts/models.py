from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=20)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True) #automatically add date,time when a user posts.

    def __str__(self):
        return self.title