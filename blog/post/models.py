from django.db import models
from django.template.defaultfilters import slugify

class Post(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100, unique=True),
    slug = models.SlugField(default='')
    text = models.TextField(default="")
    resume = models.CharField(max_length=256, blank=True, default="")

    class Meta:
        ordering = ('created_at',)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title