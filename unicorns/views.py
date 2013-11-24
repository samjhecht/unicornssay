from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse

def homepage(request):


def current_datetime(request):
    now = datetime.datetime.now()
    t = get_template('unicorns.html')
    html = t.render()
    return HttpResponse(html)
