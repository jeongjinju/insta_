# 새로 만든 것이 아닌 기존에 있던 정보를 불러오므로 import forms가 불필요
# from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    # Meta에도 UserCreationForm.Meta 상속
    # UserCreationForm 내의 Meta가 정보를 가지고 있기 때문에
    class Meta(UserCreationForm.Meta):
        model = User
        # 추가적인 column이 필요할 시 + 이후에 적어준다.
        # fields = UserCreationForm.Meta.fields + ('birth_day',)