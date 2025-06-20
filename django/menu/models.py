from django.db import models
from django.core.exceptions import ValidationError # 에러

# Create your models here.
class Menu(models.Model):
    category_choice = [('KOREAN', '한식'), ('JAPANESE', '일식'), ('CHINESE', '중식'), ('WESTERN', '양식'), ('ETC', '기타')]
    category = models.CharField(max_length=10, choices=category_choice, default='ETC')
    food = models.CharField(max_length=20, unique=True)

    def clean(self):
        # 1. 모델에 정의된 유효한 카테고리 값들만 가져옴 
        valid_db_categories = [choice[0] for choice in self.category_choice]

        # 2. 현재 저장하려는 'category' 값이 유효한 목록에 없는지 확인
        if self.category not in valid_db_categories:
            raise ValidationError( # 3. 유효하지 않다면 ValidationError를 발생시켜 저장을 막음
                {'category': f"'{self.category}'은(는 유효하지 않은 카테고리입니다. 다음 중 하나를 선택하세요: {', '.join(valid_db_categories)}"}
            )
        super().clean() # Django의 다른 기본 유효성 검사도 수행하도록 호출

    def save(self, *args, **kwargs):
        # 객체를 데이터베이스에 저장하기 전에 'clean()'을 포함한 모든 유효성 검사를 강제로 실행
        self.full_clean()
        super().save(*args, **kwargs) # 유효성 검사 통과 시 실제 저장 진행

    def __str__(self):
        return f'{self.category} : {self.food}'