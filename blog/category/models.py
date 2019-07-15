from django.db import models
from blog.post.models import Post
from django.template.defaultfilters import slugify

class Category(models.Model):
    title = models.CharField(max_length=256, unique=True)
    posts = models.ManyToManyField(Post)
    slug = models.SlugField(default='', unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name