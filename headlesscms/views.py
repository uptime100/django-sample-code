import os

from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('index.html')
    context = {
        'API_TOKEN': os.environ['BUTTERCMS_API_TOKEN']
    }
    return HttpResponse(template.render(context, request))
