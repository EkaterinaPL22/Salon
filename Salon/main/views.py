from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from django.core.mail import send_mail

from .models import Procedure, Client

from .forms import ClientForm

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
    form = ClientForm()
    template = loader.get_template('salon/make-order.html')
    context = {
        'procedures_list': procedures_list,
        'form': form
    }

    if request.method == "POST":
        form = ClientForm(request.POST)
    else:
        form = ClientForm()

    if form.is_valid():
        post = form.save(commit=False)
        post.save()

        data = form.cleaned_data

        subject = "Ваша заявка принята"
        message = data['name'] + " " + data['lastname'] + ", в ближайшее время с Вами свяжутся!"
        sender = "Kate's salon"
        recipients = ['gzmp09@gmail.com', data['email']]

        send_mail(subject, message, sender, recipients)


    return HttpResponse(template.render(context, request))