from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('firstApp.urls')),
    path('a2/', include('secondApp.urls')),
]
