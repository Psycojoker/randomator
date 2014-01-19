import json

from datetime import datetime

from django.http import HttpResponse
from django.conf.urls import patterns, url
from django.views.generic import DetailView
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
    if "id" in data and Inspiration.objects.filter(id=data["id"]).exists():
        inspiration = Inspiration.objects.get(id=data["id"])
        inspiration.name = data["name"]
        inspiration.save()
        return HttpResponse(inspiration.id)

    return HttpResponse(Inspiration.objects.create(name=data["name"]).id)



urlpatterns = patterns('',
    url(r'^list/$', inspiration_list, name='inspiration_list'),
    url(r'^add/$', add_inspiration, name='add_inspiration'),
    url(r'^get/(?P<pk>\d+)/$', DetailView.as_view(model=Inspiration), name='add_inspiration'),
)
