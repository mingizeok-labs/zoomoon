from django.shortcuts import render

from .services import RandomMenuSelectService

# Create your views here.
def random(request):
    if request.method == 'GET':
        context = {
            'msg':'test 성공'
        }
        return render(request, 'plzchoose.html', context)
    

def random_menu(request):
    if request.method == 'POST':
        random = RandomMenuSelectService()
        menu = random.random_menu_select()

        context = {'category': menu.category,
                   'food': menu.food}
        return render(request, 'plzchoose.html', context)
    
    return render(request, 'plzchoose.html')