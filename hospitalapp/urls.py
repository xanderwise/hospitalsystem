
from django.contrib import admin
from django.urls import path

from hospitalapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('starter/', views.starter, name='starter'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('department/', views.department, name='department'),
    path('doctors/', views.doctors, name='doctors'),
    path('appointment/', views.appoint, name='appoint'),
    path('contact/', views.contact, name='contact'),
]
