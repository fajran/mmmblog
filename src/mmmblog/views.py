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

def blog(request, blog_id=None):
    if blog_id is not None:
        entry = get_object_or_404(Blog, id=blog_id)
        entry.content = _apply_format(entry.content, entry.format)
        return render_to_response('blog_entry.html', {'entry': entry})
    else:
        max = 10
        entries = []
        entries += list(Blog.objects.filter(sticky=True, published=True).order_by('-date'))
        max -= len(entries)
        if max < 5:
            max = 5
        entries += list(Blog.objects.filter(sticky=False, published=True).order_by('-date')[0:max])

        for entry in entries:
            entry.content = _apply_format(entry.content, entry.format)

        return render_to_response('blog.html', {'entries': entries})

def index(request):
    return HttpResponse()
    
