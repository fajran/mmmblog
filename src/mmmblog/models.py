
from django.db import models
from django.db.models import signals
from staticgenerator import quick_publish, quick_delete

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

    def get_absolute_url(self):
        return '/blog/%i/' % self.id

class Link(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=250)
    url = models.CharField(max_length=200) # URLField doesn't allow ftp:// !
    extra = models.TextField(blank=True)
    published = models.BooleanField(default=True)
    sticky = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

def publish_blog(sender, **kwargs):
    instance = kwargs.get('instance')
    quick_publish('/')
    quick_publish('/blog/')
    quick_publish('/blog/%i/' % instance.id)

def unpublish_blog(sender, **kwargs):
    instance = kwargs.get('instance')
    quick_delete('/blog/%i/' % instance.id)
    quick_publish('/')

signals.post_save.connect(publish_blog, sender=Blog)
signals.post_delete.connect(unpublish_blog, sender=Blog)

