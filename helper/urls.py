from django.urls import path, include, re_path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
app_name = 'help'

urlpatterns = [
    path('', views.add_auto, name='home'),
    path('services/', views.services, name='services'),
    path('emergency-fuel-delivery/', views.fuel_delivery, name='fuel_delivery'),
    path('flat-tire-change/', views.flat_tire, name='flat_tire'),
    path('unlock-car-door/', views.car_unlock, name='unlock_car'),
    path('car-jump-start/', views.battery_jump_start, name='jump_start'),
    path('unfreeze-car-door/', views.unfreeze, name='unfreeze'),
    path('about/', views.about, name='about'),
    path('undo/', views.undo_all, name='undo'),
    path('add/',views.add_indi, name='add'),
    path('thankyou/', views.request_services, name='thankyou'),
    path('sitemap.xml', views.site_map, name='sitemap')

]