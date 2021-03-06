from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, PasswordChangeForm

from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import update_session_auth_hash
from .models import User

# UserCreationForm은 ModelForm > 원래 Model정보를 알아야 함
# AuthenticationForm Form을 상속받기 때문에 원래 Model 정보를 몰라도 가능하다
# 따라서 UserCreationForm은 Form을 새롭게 만들어 주었지만, 
# AuthenticationForm은 수정하지 않고 사용이 가능하다.

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/form.html', context)

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('posts:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/form.html', context)

def logout(request):
    auth_logout(request)
    return redirect("accounts:login")

def user_page(request, id):
    user_info = get_object_or_404(User, id=id)
    context = {
        'user_info': user_info
    }

    return render(request, 'accounts/user_page.html', context)

def follow(request, id):
    # 팔로우 하려는 사람, 팔로우 당하는 사람 구분 주의!
    
    # # 이미 내가 팔로우 한 상황에서 취소
    # if you.followers.filter(id=me.id):
    #     you.followers.remove(me)
    # else:
    #     you.followers.add(me)
    
    # return redirect('accounts:user_page', you.id)


    # if me.followings.filter(id=you.id):
    #     me.followings.remove(you)
    # else:
    #     me.followings.add(you
    #     )
    # return redirect('accounts:user_page', you.id)

    #----같은 역할을 하는 코드

    # 팔로우 당하는 사람, 팔로잉
    you = get_object_or_404(User, id=id)
    # 지금 로그인 한 사람, 팔로우 하려는 사람, 팔로워
    me = request.user

    if you != me:
        if me in you.followings.all():
            you.followings.remove(me)
        else:
            you.followings.add(me)
    return redirect('accounts:user_page', you.id)




def delete(request, id):
    # 보고 있는 페이지의 유저 정보
    if request.method == "POST":
        user_info = get_object_or_404(User, id=id)
        user = request.user

        if user == user_info:
            user.delete()
        return redirect('posts:index')
    else:
        return redirect('accoutns:user_page',id)


def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('posts:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
        # 이렇게 가져온 폼에는 
        # 사용자가 임의로 건들여선 안 되는 정보도 함께 가져오게 된다.
    context = {
        'form':form
    }
    return render(request, 'accounts/form.html', context)

def password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            # 비밀번호가 바뀌면서 세션이 바뀌어
            # index페이지로 가면 로그아웃된 상태가 된다.
            # 이를 해결하기 위함.
            update_session_auth_hash(request, form.user)
            return redirect('posts:index')

    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form':form
    }
    return render(request, 'accounts/form.html', context)


def profile(request):
    user_info = request.user
    context = {
        'user_info': user_info
    }

    return render(request, 'accounts/user_page.html', context)


def try_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('posts:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/try_login.html', context)