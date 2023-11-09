from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UserEditForm(forms.ModelForm):
    """форма редактирования пользователя"""

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]


class ProfileEditForm(forms.ModelForm):
    """форма редактирования профиля"""

    class Meta:
        model = Profile
        fields = ["date_of_birth", "photo"]


class LoginForm(forms.Form):
    """форма для входа в аккаунт"""

    username = forms.CharField(label="Имя пользователя")
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль")


class UserRegistrationForm(forms.ModelForm):
    """форма регистрации пользователя"""

    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Повторите пароль", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ["username", "first_name", "email"]

    def clean_password2(self):
        """валидация подтверждения пароля"""
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("Пароли не совпадают")
        return cd["password2"]
