from django.shortcuts import render, redirect

# Create your views here.
from .models import Menu, Category

def totalmenu_view(request):
    all_category = Category.objects.all().order_by('code') # 카테고리 목록
    all_food = Menu.objects.all() # 음식 목록
    return render(request, 'totalmenu_view.html', {'menus': all_food, 'category': all_category})

def add_menu(request):
    # if add_menu:
    #     all_category = Category.objects.all()
    #     return render(request, 'add_menu.html', {'category':all_category})

    all_category = Category.objects.all()
    if request.method == 'GET':
        context = {'msg1' : '알잘딱깔센! 카테고리 선택과 메뉴 이름을 작성해주세요 :)', 'category': all_category}
        return render(request, 'add_menu.html', context)

    elif request.method == 'POST':
        category_id = request.POST.get('category_id')
        food = request.POST.get('food')
        
        if category_id and food: # 데이터 존재 여부 파악
            select_cat = Category.objects.get(id=category_id)
            Menu.objects.create(food=food, category=select_cat)
            return redirect('success_page_or_menu_list') # 리다이렉트할 URL 이름으로 변경 (예: 'menu_list')
        else: # 누락 시
            context = {'errormsg' : "메뉴 이름과 카테고리를 모두 입력해주세요."}
            return render(request, 'add_menu.html', context)
    