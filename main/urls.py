from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('club/', views.clubSelection, name='club'),
    path('national/', views.nationalSelection, name='national'),
    path('<str:type>/<slug:slug>', views.viewJersey, name='view'),
]