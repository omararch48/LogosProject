from django.urls import path

from . import views


urlpatterns = [
    # Paths core
    path('', views.us, name='us'),
    path('text/<int:text_id>/', views.text, name='text'),
]
