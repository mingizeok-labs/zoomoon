from django.urls import path
from . import views # plzchoose/view.py

app_name = 'plzchoose'

urlpatterns = [
    path('', views.random_menu, name='random')
]