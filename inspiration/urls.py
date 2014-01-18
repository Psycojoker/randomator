import json

from datetime import datetime

from django.conf.urls import patterns, url
from django.http import HttpResponse
from .models import Inspiration


def datetime_serializer(value):
    if isinstance(value, datetime):
        return value.strftime("%F %X")
    return value

def inspiration_list(request):
    return HttpResponse(json.dumps(list(Inspiration.objects.all().values()), default=datetime_serializer))


urlpatterns = patterns('',
    url(r'^list/$', inspiration_list, name='inspiration_list'),
)
