from django.urls import path
from . import views 

app_name = 'app'

urlpatterns = [
    path('', views.home, name='homepage'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),


]