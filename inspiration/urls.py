import json

from datetime import datetime

from django.http import HttpResponse
from django.conf.urls import patterns, url
from django.views.decorators.csrf import csrf_exempt

from .models import Inspiration


def datetime_serializer(value):
    if isinstance(value, datetime):
        return value.strftime("%F %X")
    return value


def inspiration_list(request):
    return HttpResponse(json.dumps(list(Inspiration.objects.filter(active=True).values()), default=datetime_serializer))


@csrf_exempt
def add_inspiration(request):
    data = json.loads(request.body)
    result = Inspiration.objects.create(name=data["name"])
    return HttpResponse(result.id)


urlpatterns = patterns('',
    url(r'^list/$', inspiration_list, name='inspiration_list'),
    url(r'^add/$', add_inspiration, name='add_inspiration'),
)
