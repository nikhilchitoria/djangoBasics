from django.urls import path
from . import views

urlpatterns = [
    path('greet', views.greet, name='greet'),
    path('hello', views.Hello.as_view(), name='hello'),
    path('', views.home, name='home'),
]
