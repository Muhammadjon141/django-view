from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# class RegisterForm(UserCreationForm):
#     username = forms.CharField(required=True)

#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'username', 'email', 'password']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')