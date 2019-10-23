from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# 원래 형태로 보기 위함
from .models import User
# Register your models here.
admin.site.register(User, UserAdmin)