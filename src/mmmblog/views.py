from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from mmmblog.models import Blog, Link

def _apply_format(content, format):
    if format == 'markdown':
        import markdown
        return markdown.markdown(content)
    else:
        return content

def _get_blog_entries(max=10, min=5):
    entries = []
    entries += list(Blog.objects.filter(sticky=True, published=True).order_by('-date'))
    max -= len(entries)
    if max < min:
        max = min
    entries += list(Blog.objects.filter(sticky=False, published=True).order_by('-date')[0:max])

    for entry in entries:
        entry.content = _apply_format(entry.content, entry.format)

    return entries

def _get_links(max=10, min=5):
    links = []
    links += list(Link.objects.filter(sticky=True, published=True).order_by('-date'))
    max -= len(links)
    if max < min:
        max = min
    links += list(Link.objects.filter(sticky=False, published=True).order_by('-date')[0:max])

    return links

def blog(request, blog_id=None):
    if blog_id is not None:
        entry = get_object_or_404(Blog, id=blog_id)
        entry.content = _apply_format(entry.content, entry.format)
        return render_to_response('blog_entry.html', {'entry': entry})
    else:
        entries = _get_blog_entries(10)
        return render_to_response('blog.html', {'entries': entries})

def index(request):
    entries = _get_blog_entries(2, 2)
    links = _get_links(10, 5)
    return render_to_response('index.html', {'entries': entries, 'links': links})
    
