from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_gestock.urls')), # Get urls from the app : app_gestock
]