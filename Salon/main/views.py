from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Procedure, Client

# Create your views here.

def index(request):
    procedures_list = Procedure.objects.all()
    template = loader.get_template('salon/index.html')
    context = {
        'procedures_list': procedures_list,
    }
    return HttpResponse(template.render(context, request))


def make_order(request):
    procedures_list = Procedure.objects.all()
    template = loader.get_template('salon/make-order.html')
    context = {
        'procedures_list': procedures_list,
    }
    return HttpResponse(template.render(context, request))