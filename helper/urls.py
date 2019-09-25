from django.urls import path, include, re_path
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.views.generic import TemplateView

from . import views
app_name = 'help'

urlpatterns = [
    path('', views.add_auto,  name='home'),
    path('Car-Unlock-Service-Chicago-IL/', views.car_unlock, name='unlock_car'),
    path('Jump-Start-Service-Illinois-Chicago/', views.battery_jump_start, name='jump_start'),
    path('Pasar-Cables-Chicago-IL/', views.jump_service_spanish, name='spanish'),
    path('roadside-assistance-chicago-illinois/', views.roadside_assistance, name='roadside_assistance'),
    path('sitemap.html/', views.user_sitemap, name='user_sitemap'),
    path('thankyou/', views.request_services, name='thankyou'),
    path('sitemap.xml', views.site_map, name='sitemap'),
    path('robots.txt', TemplateView.as_view(template_name="helper/robots.txt", content_type="text/plain"),
         name="robots_file")
]


