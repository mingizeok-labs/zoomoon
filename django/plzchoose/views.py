from django.shortcuts import render

# Create your views here.
def random(request):
    if request.method == 'GET':
        context = {
            'msg':'test 성공'
        }
        return render(request, 'plzchoose.html', context)