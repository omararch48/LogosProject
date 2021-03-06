from django.urls import path

from . import views


urlpatterns = [
    # Paths products
    path('', views.categories, name='services'),
    path('<category_name>/', views.services, name='services_list'),
    path(
        '<category_name>/<int:service_id>/', 
        views.service, 
        name='services_list_detail'
    ),
]