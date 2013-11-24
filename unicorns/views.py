from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse

def homepage(request):

    # t = get_template('unicorns.html')
    # html = t.render()
    # return HttpResponse(html)
    return render(request, 'unicorns.html')
