from django.urls import path
from . import views

urlpatterns = [
    path('auth_code/', views.auth_code, name='auth_code'),
    path('callback/', views.callback, name='callback'),
]