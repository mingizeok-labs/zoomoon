from django.shortcuts import render

# Create your views here.
from .models import Menu, Category

def totalmenu_view(request):
    all_category = Category.objects.all().order_by('code') # 카테고리 목록
    all_food = Menu.objects.all() # 음식 목록
    return render(request, 'totalmenu_view.html', {'menus': all_food, 'category': all_category})