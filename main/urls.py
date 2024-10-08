from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.main_view, name='main_view_url'),
    path('create-product/', views.create_product, name='create_product_url'),
    path('edit-product/<uuid:id>', views.edit_product, name='edit_product_url'),
    path('delete/<uuid:id>', views.delete_product, name='delete_product_url'),
    path('xml/', views.show_xml, name='show_xml_url'),
    path('json/', views.show_json, name='show_json_url'),
    path('xml/<str:id>', views.show_xml_by_id, name='show_xml_by_id_url'),
    path('json/<str:id>', views.show_json_by_id, name='show_json_by_id_url'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('create-product-ajax', views.add_product_ajax, name='add_product_ajax'),
]