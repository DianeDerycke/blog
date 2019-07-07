from django.db import models

# Create your models here.


class Post(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100)
    text = models.TextField(default="")
    resume = models.CharField(max_length=256, blank=True, default="")

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        return self.title + " - " + str(self.category)

class Category(models.Model):
    name = models.CharField(max_length=256)
    posts = models.ManyToManyField(Post)

    def __str__(self):
        return self.name