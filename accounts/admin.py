from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Follow

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username',]
    fieldsets =  UserAdmin.fieldsets + (
        ("Extra information", {"fields": ("phonenumber",'gender','profilePicture','interests', 'user'),},
        
        ),
    )

    # def save_model(self, request, obj, form, change):
    #     obj.user = request.user
    #     obj.save()

class FollowAdmin(admin.ModelAdmin):
    list_display = ['to_user', 'from_user',]
    model = Follow

    def save_model(self, request, obj, form, change):
        
        if obj.from_user != obj.to_user:
            obj.from_user = request.user
            obj.save()

# filter duplicate relationships in frontend, by looping through all objects.

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Follow, FollowAdmin)
