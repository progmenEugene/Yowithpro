from django import forms
from .models import User, TeacherProfile


class RegistrationForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['email', ]




class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email']


class TeacherProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = TeacherProfile
        fields = ['image','name','city', 'club', 'url_youtube', 'description']