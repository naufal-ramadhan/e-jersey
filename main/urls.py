from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.main_view, name='main_view_url'),
    path('create-product/', views.create_product, name='create_product_url'),
    path('xml/', views.show_xml, name='show_xml_url'),
    path('json/', views.show_json, name='show_json_url'),
    path('xml/<str:id>', views.show_xml_by_id, name='show_xml_by_id_url'),
    path('json/<str:id>', views.show_json_by_id, name='show_json_by_id_url'),
]