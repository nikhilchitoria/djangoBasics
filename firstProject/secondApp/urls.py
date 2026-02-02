from django.urls import path
from . import views

urlpatterns = [
    path('firstpage', views.first_page, name='firstpage'),
    path('secondpage', views.second_page, name='secondpage'),
]
