from django.db import models

# Create your models here.
class Menu(models.Model):
    category_choice = [('KOREAN', '한식'), ('JAPANESE', '일식'), ('CHINESE', '중식'), ('WESTERN', '양식'), ('ETC', '기타')]
    category = models.CharField(max_length=10, choices=category_choice, default='기타')
    food = models.CharField(max_length=20)
    def __str__(self):
        return f'{self.category} : {self.food}'