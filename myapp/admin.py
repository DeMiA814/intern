from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, MyUserManager

admin.site.register(User, UserAdmin)
#,UserAdmin
