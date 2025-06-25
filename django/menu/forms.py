# 사용자가 입력하는 정보를 처리하기 위해 django의 forms 모듈을 사용한다!
# 일반적으로 ModelForm을 사용한다..?

from django import forms # djanog.forms 모듈 사용
from .models import Menu, Category # 데이터를 받아와 어디에 저장할것인지 설정하기 위함.

class AddMenu(forms.ModelForm):
    class Meta:
        model = Menu # 저장할 DB
        fields = '__all__'

        widgets = {
            'category': forms.Select(attrs={
                'class': 'add_cat'
            }),
            'food': forms.TextInput(attrs={
                'class': 'add_food',
                'placeholder': '추가하고 싶은 메뉴를 입력하세요:)'
            })
        }