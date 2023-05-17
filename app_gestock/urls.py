from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('product', views.product, name = 'product'),
    path('accounts/', include('django.contrib.auth.urls')), #Django site authentication urls (for login, logout, password management)
]