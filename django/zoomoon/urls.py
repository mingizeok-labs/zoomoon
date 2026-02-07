from django.urls import path
from . import views # zoomoon/views.py

app_name = 'zoomoon' # name space 지정

urlpatterns = [
    path('', views.main_view, name='main'),
]