from django.urls import path, include, re_path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
app_name = 'help'

urlpatterns = [
    path('', views.add_auto, name='home'),
    path('fuel-delivery/', views.fuel_delivery, name='fuel_delivery'),
    path('car-unlock-service/', views.car_unlock, name='unlock_car'),
    path('jump-start-car/', views.battery_jump_start, name='jump_start'),
    path('unfreeze-car-door/', views.unfreeze, name='unfreeze'),
    path('about/', views.about, name='about'),
    path('undo/', views.undo_all, name='undo'),
    path('add/',views.add_indi, name='add'),
    path('thankyou/', views.request_services, name='thankyou'),
    path('sitemap.xml', views.site_map, name='sitemap')

]