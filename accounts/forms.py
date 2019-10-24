# 새로 만든 것이 아닌 기존에 있던 정보를 불러오므로 import forms가 불필요
# from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from django.contrib.auth import get_user_model
class CustomUserCreationForm(UserCreationForm):
    # Meta에도 UserCreationForm.Meta 상속
    # UserCreationForm 내의 Meta가 정보를 가지고 있기 때문에
    class Meta(UserCreationForm.Meta):
        model = User
        # 추가적인 column이 필요할 시 + 이후에 적어준다.
        # fields = UserCreationForm.Meta.fields + ('birth_day',)


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        # User == get_user_model 
        # 결과적으로 같은 의미를 가지고 있다.
        # settings.AUTH_USER_MODEL 
        # >> 모델을 str 으로 알려줌, str정보를 가지고 있는 것
        # get_user_model 
        # >> class를 반환, 따라서 설정 시 class값을 넣어주어야함.
        # 즉 return값이 다르다.
        fields = ('first_name', 'last_name', "email",)