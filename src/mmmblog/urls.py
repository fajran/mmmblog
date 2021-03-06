from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^\+media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'^admin/', include(admin.site.urls)),
    (r'^blog/$', 'mmmblog.views.blog'),
    (r'^blog/(?P<blog_id>\d+)/$', 'mmmblog.views.blog'),
    (r'^$', 'mmmblog.views.index')
)
