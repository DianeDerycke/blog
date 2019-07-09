from django.db import models
from blog.post.models import Post

class Category(models.Model):
    name = models.CharField(max_length=256)
    posts = models.ManyToManyField(Post)

    def __str__(self):
        return self.name