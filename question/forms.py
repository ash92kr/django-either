from django import forms
from .models import Question, Comment   # 현재 폴더 아래 있는 Question class를 import시켜 model에 넣음

class QuestionForm(forms.ModelForm):   # forms의 ModelForm을 상속시킴
    class Meta:
        model = Question
        fields = ['title', 'answerA', 'answerB']
        
class CommentForm(forms.ModelForm):
    class Meta:       
        model = Comment
        fields = ['answer', 'content']  # id가 없어서 저장 불가 