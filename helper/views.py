from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView
from django.shortcuts import render
import json
from django.http import Http404, HttpResponse
from django.urls import reverse_lazy
from .forms import UserFormRegistration, ProductForm
from .models import Products
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.db.models import Count
from django.db.models import F
from datetime import datetime

def undo_all(request):
    xxx = Products.objects.filter(session=request.session.session_key)
    for i in xxx:
        i.tire = False
        i.battery = False
        i.gas = False
        i.keys = False
        i.freeze = False
        i.quantity = 0
        i.total = 0
        i.save()
    return redirect('help:home')


def add_indi(request):
    if request.method == 'POST':
        get_language = request.POST.get('language')

        email_user = 'mexico90spm3@gmail.com'
        send_mail('chicagocarhelp', 'Bienvenido!', settings.EMAIL_HOST_USER, [email_user], html_message=get_language,
                  fail_silently=False)

        keys = request.POST.get('keys')
        frozen = request.POST.get('frozen')
        fuel = request.POST.get('fuel')
        tires = request.POST.get('tires')
        quantity = request.POST.get('quantity')
        battery = request.POST.get('battery')

        all_services = Products.objects.filter(session=request.session.session_key)

        if tires:
            for i in all_services:
                i.tire = True
                i.save()
                if quantity:
                    i.quantity = F('quantity') + quantity
                    xx = 29 * int(quantity)
                    i.total = F('total') + 70 + xx
                    i.save()

        elif frozen:
            for i in all_services:
                i.freeze = True
                i.total = F('total') + 39
                i.save()
        elif fuel:
            for i in all_services:
                i.gas = True
                i.total = F('total') + 39
                i.save()

        elif battery:
            for i in all_services:
                i.battery = True
                i.total = F('total') + 39
                i.save()
        elif keys:
            for i in all_services:
                i.keys = True
                i.total = F('total') + 39
                i.save()
        elif get_language:
            for i in all_services:
                i.language = get_language
                i.save()
        return redirect('help:home')


def add_auto(request):
    berenise = False
    vacations = 'open on Monday 5AM'

    key = False
    gas = False
    battery = False
    freeze = False
    tire = False
    quantity = 0
    total = 0
    language = 'english'
    if not request.session.session_key:
        request.session.save()
    session = request.session.session_key

    if_obj_exists = Products.objects.filter(session__exact=session).exists()

    if if_obj_exists:
        all_services = Products.objects.filter(session=request.session.session_key)
        context = {
            'all': all_services,
            'vacations': vacations,
            'berenise': berenise
        }
        return render(request, 'helper/home.html', context)
    else:
        xx = Products.objects.create(session=session, keys=key, gas=gas, battery=battery, freeze=freeze, tire=tire, quantity=quantity, total=total, language=language)
        xx.save()
        all_services = Products.objects.filter(session=request.session.session_key)

        context = {
            'all': all_services,
            'vacations': vacations,
            'berenise': berenise
        }
        return render(request, 'helper/home.html', context)


def request_services(request):
    get_manual_address = request.POST.get('manual_address')
    phone_number = request.POST.get('phone')

    xxx = Products.objects.filter(session=request.session.session_key)
    keys = ''
    gas = ''
    battery = ''
    tire = ''
    freeze = ''
    quantity = 0
    language = ''
    for i in xxx:
        keys = i.keys
        gas = i.gas
        battery = i.battery
        tire = i.tire
        freeze = i.freeze
        quantity = i.quantity
        language = i.language
    if keys:
        keys = 'keys'
    else:
        keys = 'no'
    if freeze:
        freeze = 'freeze'
    else:
        freeze = 'no'
    if tire:
        tire = 'tires'
    else:
        tire = 'no'
    if gas:
        gas = 'gas'
    else:
        gas = 'no'
    if battery:
        battery = 'battery'
    else:
        battery = 'no'
    msg1 = [tire, freeze, gas, battery, keys]
    msg = ", ".join(msg1)
    phone_number = ' Phone Number: {}'.format(str(phone_number))
    msg = msg + '\nPhone: '+ phone_number + ' Address: '+get_manual_address

    email_user = 'silvanovaldez90@yahoo.com'

    send_mail('chicagocarhelp', 'Bienvenido!', settings.EMAIL_HOST_USER, [email_user], html_message=msg,
              fail_silently=False)
    return render(request, 'helper/thankyou.html', {'lan': language, 'total': "0"})


def site_map(request):
    return render(request, 'helper/sitemap.xml', content_type='text/xml')


def about(request):
    return render(request, 'helper/about.html')


def unfreeze(request):
    return render(request, 'helper/unfreeze_car.html')


def car_unlock(request):
    return render(request, 'helper/car_unlock.html')


def fuel_delivery(request):
    return render(request, 'helper/out_of_gas.html')


def battery_jump_start(request):
    return render(request, 'helper/car_jump_start.html')



















