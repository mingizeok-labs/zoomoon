from django.urls import path
from . import views # plzchoose/view.py

urlpatterns = [
    path('', views.random, name='random')
]