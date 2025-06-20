from django.shortcuts import render

# Create your views here.
from .models import Menu

def totalmenu_view(request):
    all_menus = Menu.objects.all() # 등록된 전체 메뉴 목록
    return render(request, 'totalmenu_view.html', {'menus': all_menus})