from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username',]
    fieldsets =  UserAdmin.fieldsets + (
        ("Extra information", {"fields": ("phonenumber",'gender','profilePicture','interests', 'user'),},
        
        ),
    )
    def save_model(self, request, obj, form, change):
        print(request.user)
        obj.user = request.user
        obj.save()
        print(obj.user)


admin.site.register(CustomUser, CustomUserAdmin)