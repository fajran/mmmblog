
from django.db import models

FORMAT_CHOICES = (
    ('html', 'Raw HTML'),
    ('markdown', 'Markdown'),
)

class Blog(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    format = models.CharField(max_length=10, choices=FORMAT_CHOICES)
    published = models.BooleanField(default=True)
    sticky = models.BooleanField(default=False)

class Link(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=250)
    url = models.URLField()
    extra = models.TextField(blank=True)
    published = models.BooleanField(default=True)
    sticky = models.BooleanField(default=False)

