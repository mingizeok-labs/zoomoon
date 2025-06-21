from django.urls import path
from . import views # menu/views.py

app_name = 'menu' # name space 지정

urlpatterns = [
    path('totalmenu_view', views.totalmenu_view, name='totalmenu_view'),
    path('add', views.menu_add, name='menu_add'),
]