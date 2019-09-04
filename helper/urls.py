from django.urls import path, include, re_path
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.views.generic import TemplateView

from . import views
app_name = 'help'

urlpatterns = [
    path('', views.add_auto,  name='home'),
    path('car-unlock-service/', views.car_unlock, name='unlock_car'),
    path('jump-start-car/', views.battery_jump_start, name='jump_start'),
    path('Pasar-Cables-Chicago-IL/', views.jump_service_spanish, name='spanish'),
    path('undo/', views.undo_all, name='undo'),
    path('add/',views.add_indi, name='add'),
    path('thankyou/', views.request_services, name='thankyou'),
    path('sitemap.xml', views.site_map, name='sitemap'),
    path('robots.txt', TemplateView.as_view(template_name="helper/robots.txt", content_type="text/plain"),
         name="robots_file")

]


