from django.shortcuts import render
import calendar
from datetime import datetime
from django.http import HttpResponseRedirect
from .forms import FormandoForm


# Create your views here.

def home(request):
    return render(request, 'base/home.html')


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



