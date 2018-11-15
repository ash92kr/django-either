from django.db import models
from django.conf import settings

# Create your models here.
class Question(models.Model):  # models.Model을 상속받음
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  
    title = models.CharField(max_length=50)            # 필수 작성 사항 -> AUTH_USER_MODEL = auth.user(기본 user 모델 사용)
    answerA = models.CharField(max_length=50)
    answerB = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title  # 오버라이드

class Comment(models.Model):                                        # 2번을 선택했을 때
    question = models.ForeignKey(Question, on_delete=models.CASCADE)   # 질문이 사라지면 댓글도 모두 사라진다
    answer_list = [['A', 'left'], ['B', 'right']]   # 사용자가 어떤 선택을 할 수 있는지 선택지 제공
    answer = models.CharField(max_length=50, choices=answer_list)
    content = models.CharField(max_length=50)

    def __str__(self):
        return self.content