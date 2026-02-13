from django.shortcuts import render, redirect

# Create your views here.
from .forms import AddMenu # html input 가져오기 위함.
from .models import Menu, Category

def totalmenu_view(request):
    all_category = Category.objects.all().order_by('code') # 카테고리 목록
    all_food = Menu.objects.all().order_by('category__code') # 음식 목록
    return render(request, 'totalmenu_view.html', {'menus': all_food, 'category': all_category})

def add_menu(request):
    all_category = Category.objects.all() # GET 요청 시
    if request.method == 'POST':
        form = AddMenu(request.POST) # form 작성한걸 html로 넘기기
        if form.is_valid():
            menu_item = form.save() 
            return redirect('menu:totalmenu_view') # 저장 후 리디렉션
        # return render(request, 'add_menu.html',{'msg':'저장이 완료되었습니다'})
        else: # 중복된 데이터 입력 시
            context = {
                'form': form, # 오류가 있는 폼을 템플릿으로 다시 보냅니다.
                'msg1': '중복된 데이터가 존재합니다.',
                'category': all_category # 카테고리 목록도 다시 전달
            }
            return render(request, 'add_menu.html', context)
    elif request.method == 'GET':
        # GET 요청 시, 빈 폼을 생성하여 템플릿으로 보냄
        form = AddMenu()
        context = {
            'form': form,
            'msg1': '알잘딱깔센! 카테고리 선택과 메뉴 이름을 작성해주세요 :)',
            'category': all_category
        }
        return render(request, 'add_menu.html', context)