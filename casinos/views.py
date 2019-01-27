from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Casino
from .models import Bonus
from django.http import Http404
def index(request):
    template = loader.get_template('casinos/index.html')
    context = {
        'text': "wellcome page!",
    }
    return HttpResponse(template.render(context, request))

def casinos(request):
    latest_casino_list = Casino.objects.order_by('-date_added')[:5]
    template = loader.get_template('casinos/casinos.html')
    context = {
        'latest_casino_list': latest_casino_list,
    }
    return HttpResponse(template.render(context, request))


def cinfo(request, casino_id):
    try:
        casino = Casino.objects.get(pk=casino_id)
    except Casino.DoesNotExist:
        raise Http404("Casino does not exist")
    return render(request, 'casinos/cinfo.html', {'casino': casino})

def bonuses(request):
    latest_bonus_list = Bonus.objects.order_by('-date_added')[:5]
    template = loader.get_template('casinos/bonuses.html')
    context = {
        'latest_bonus_list': latest_bonus_list,
    }
    return HttpResponse(template.render(context, request))

def binfo(request, bonus_id):
    try:
        bonus = Bonus.objects.get(pk=bonus_id)
    except Casino.DoesNotExist:
        raise Http404("Bonus does not exist")
    return render(request, 'casinos/binfo.html', {'bonus': bonus, 'casino': Casino.objects.get(pk=bonus.casino_id)})
