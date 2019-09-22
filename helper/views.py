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
from django.views.decorators.cache import cache_page
import time


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

        ll = render(request, 'helper/home.html', context)
        ll['Cache-Control'] = 'public,max-age=10000'
        return ll
    else:
        xx = Products.objects.create(session=session, keys=key, gas=gas, battery=battery, freeze=freeze, tire=tire, quantity=quantity, total=total, language=language)
        xx.save()
        all_services = Products.objects.filter(session=request.session.session_key)

        context = {
            'all': all_services,
            'vacations': vacations,
            'berenise': berenise
        }

        ll = render(request, 'helper/home.html', context)
        ll['Cache-Control'] = 'public,max-age=10000'
        return ll


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
    msg = phone_number + "\nAddress: "+str(get_manual_address)

    email_user = 'silvanovaldez90@yahoo.com'

    send_mail('chicagocarhelp', 'Bienvenido!', settings.EMAIL_HOST_USER, [email_user], html_message=msg,
              fail_silently=False)
    return render(request, 'helper/thankyou.html', {'lan': language, 'total': "0"})


def site_map(request):
    return render(request, 'helper/sitemap.xml', content_type='text/xml')


def car_unlock(request):
    return render(request, 'helper/car_unlock.html')


def battery_jump_start(request):
    return render(request, 'helper/car_jump_start.html')


def jump_service_spanish(request):
    return render(request, 'helper/spanish.html')


def user_sitemap(request):
    return render(request, 'helper/spanish.html')



















