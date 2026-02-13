from django.urls import path
from . import views # menu/views.py

app_name = 'menu' # name space 지정

urlpatterns = [
    path('', views.totalmenu_view, name='totalmenu_view'),
    path('add', views.add_menu, name='add_menu'),
]