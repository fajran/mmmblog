from django.contrib import admin
from mmmblog.models import Blog, Link

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'published', 'sticky')

class LinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'date', 'published', 'sticky')

admin.site.register(Blog, BlogAdmin)
admin.site.register(Link, LinkAdmin)

