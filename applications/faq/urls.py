from django.urls import path

from . import views


urlpatterns = [
    # Paths products
    path('', views.faq, name='faq'),
]
