from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.template import loader

from blogging.models import Post
# Create your views here.

def stub_view(request, *args, **kwargs):
    body = "Stub View\n\n"
    if args:
        body += "Args:\n"
        body += "\n".join(["\t%s" % a for a in args])
    if kwargs:
        body += "Kwargs:\n"
        body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])
    return HttpResponse(body, content_type="text/plain")

class BlogListView(ListView):
    queryset = Post.objects.exclude(publish_datetime__exact=None).order_by('-publish_datetime')
    # in addtion to getting lower-cased model name + _list "like object_list, post_list"... you can define context_object_name
    # read more about context_object_name:
    #  https://docs.djangoproject.com/en/2.1/topics/class-based-views/generic-display/#making-friendly-template-contexts
    context_object_name = 'reverse_published_posts'
    template_name = 'blogging/list.html'

# def list_view(request):
#     published = Post.objects.exclude(publish_datetime__exact=None)
#     posts = published.order_by('-publish_datetime')
#     template = loader.get_template('blogging/list.html')
#     context = {'posts': posts}
#     body = template.render(context)
#     return HttpResponse(body, content_type="text/html")

    # rewrite our view with render shortcut provided by Django
    # return render(request, 'blogging/list.html', context)

def detail_view(request, post_id):
    #__exact just seems to be explicit "exact"... not necessary
    published = Post.objects.exclude(publish_datetime=None)
    try:
        post = published.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404
    context = {'post': post}
    return render(request, 'blogging/detail.html', context)