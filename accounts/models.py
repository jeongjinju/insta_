from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

# AbstractUser을 상속받아 M대N으로 follow column 추가
class User(AbstractUser):
    # class 내부에서 User를 다시 호출하는 건 불가능
    # settings.AUTH_USER_MODEL : 자기 자신이 아닌 기본 설정 
    # 해결 : 
    # auth app안에 있는 user 모델 > settings.py > AUTH_USER_MODEL 변수 설정
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="followings")