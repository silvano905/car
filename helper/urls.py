from django.urls import path, include, re_path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
app_name = 'help'

urlpatterns = [
    path('', views.add_auto, name='services'),
    path('undo/', views.undo_all, name='undo'),
    path('add/',views.add_indi, name='add'),
    path('thankyou/', views.request_services, name='thankyou')
]