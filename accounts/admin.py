from django.contrib import admin

# Register your models here.
from .models import User, TeacherProfile


class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'is_staff', 'is_active']


class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name']



admin.site.register(User, UserAdmin)
admin.site.register(TeacherProfile, TeacherAdmin)