from django.db import models

# Create your models here.
class Question(models.Model):  # models.Model을 상속받음
    title = models.CharField(max_length=50)
    answerA = models.CharField(max_length=50)
    answerB = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title  # 오버라이드

class Comment(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)   # 질문이 사라지면 댓글도 모두 사라진다
    answer_list = [['A', 'left'], ['B', 'right']]   # 사용자가 어떤 선택을 할 수 있는지 선택지 제공
    answer = models.CharField(max_length=50, choices=answer_list)
    content = models.CharField(max_length=50)

    def __str__(self):
        return self.content