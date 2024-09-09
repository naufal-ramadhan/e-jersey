from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.dataDiri, name='datadiri'),
    path('club/', views.clubSelection, name='club'),
    path('national/', views.nationalSelection, name='national'),
    path('<str:type>/<slug:slug>', views.viewJersey, name='view'),
]