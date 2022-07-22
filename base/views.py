from django.shortcuts import render
import calendar
from datetime import datetime
from django.http import HttpResponseRedirect
from .forms import FormandoForm
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings


# Create your views here.

def home(request):

    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        # send email
        send_mail(
            message_name,
            message,
            message_email,
            ['joaodcarvalho2017@gmail.com'],
            fail_silently=False,
        )

        return render(request, 'base/home.html', {'message_name':message_name})

    else:
        return render(request, 'base/home.html', {})




def formandos(request):
    submitted = False
    if request.method == 'POST':
        form = FormandoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/formandos?submitted=True')
    else:
        form = FormandoForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'base/formandos.html', {'form': form, 'submitted': submitted})







