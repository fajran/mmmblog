
from django.db import models

FORMAT_CHOICES = (
    ('html', 'Raw HTML'),
    ('markdown', 'Markdown'),
)

class Blog(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=250)
    content = models.TextField()
    format = models.CharField(max_length=10, choices=FORMAT_CHOICES, default='html')
    published = models.BooleanField(default=True)
    sticky = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

class Link(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=250)
    url = models.CharField(max_length=200) # URLField doesn't allow ftp:// !
    extra = models.TextField(blank=True)
    published = models.BooleanField(default=True)
    sticky = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

