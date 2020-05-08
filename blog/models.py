from django.conf import settings
from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField


class Post(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=100)
    published_date = models.DateTimeField(default=timezone.now)
    content = HTMLField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
