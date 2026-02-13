"""
랜덤으로 출력하는 로직 제작
"""
import random
from menu.models import Menu

class RandomMenuSelectService:
    def __init__(self):
        self.menu = Menu.objects.all() # 음식 목록
        
    def random_menu_select(self):
        return random.choice(self.menu)
    