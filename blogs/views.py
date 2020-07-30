import os

from butter_cms import ButterCMS
from django.http import HttpResponse
from django.template import loader

client = ButterCMS(os.environ['BUTTERCMS_API_TOKEN'])


def index(request):
    template = loader.get_template('blogs_index.html')
    response = client.posts.all({'page': 1, 'page_size': 10, 'order': '-date_published'})
    posts = response['data']
    context = {
        'posts': posts,
    }
    return HttpResponse(template.render(context, request))


def post(request, slug):
    template = loader.get_template('blogs_post.html')
    response = client.posts.get(slug)
    post = response['data']
    context = {
        'post': post,
    }
    print(post)
    return HttpResponse(template.render(context, request))
