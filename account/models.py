from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)       # User의 id와 email에 관한 것과 일대일 관계
    nickname=models.CharField(max_length=50)
    birth_date=models.DateField()
    
    
    
    
    
    
    