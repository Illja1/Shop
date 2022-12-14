from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from captcha.fields import CaptchaField,CaptchaTextInput


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='User name', widget = forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Password', widget = forms.PasswordInput(attrs={'class':'form-control'}))
    captcha = CaptchaField()


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='User name', help_text='User name must be 150 characters',widget = forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Password', help_text='User name at least must be 8 characters and contains number and symbols',widget = forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm password',help_text='Password must match',widget = forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label="E-mail",widget = forms.EmailInput(attrs={'class':'form-control'}))
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1','password2')
