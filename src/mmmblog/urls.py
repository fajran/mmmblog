from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # (r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'homepage.html'}),
    # (r'^\+media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    # Example:
    # (r'^epiweb/', include('epiweb.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^blog/$', 'mmmblog.views.blog'),
    (r'^blog/(?P<blog_id>\d+)/$', 'mmmblog.views.blog'),
    (r'^$', 'mmmblog.views.index')
)
