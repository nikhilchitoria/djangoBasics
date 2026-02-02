from django.urls import path
from . import views

urlpatterns = [
    path('greet', views.greet),
    path('hello', views.Hello.as_view()),
    path('home', views.home),
]
