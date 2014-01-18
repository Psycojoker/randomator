from django.db import models


class Inspiration(models.Model):
    name = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
