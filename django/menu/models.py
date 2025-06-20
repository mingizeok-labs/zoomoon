from django.db import models
from django.core.exceptions import ValidationError # 에러

# Create your models here.
class Category(models.Model):
    code = models.IntegerField(default=0, unique=True) # 정렬 순서 지정 (1 ~> )
    name = models.CharField(max_length=20, unique=True, verbose_name='DB 카테고리')
    display_name = models.CharField(max_length=10, unique=True, verbose_name='카테고리')
    # 정렬
    class Meta:
        ordering = ['code']
    def __str__(self):
        return self.display_name

class Menu(models.Model):
    # category_choice = [('KOREAN', '한식'), ('JAPANESE', '일식'), ('CHINESE', '중식'), ('WESTERN', '양식'), ('ETC', '기타')]
    # category = models.CharField(max_length=10, choices=category_choice, default='ETC')
    # -> 카테고리 Table 생성으로 삭제
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='카테고리')
    food = models.CharField(max_length=20, unique=True)
    
    def __str__(self):
        return f'{self.category} : {self.food}'
