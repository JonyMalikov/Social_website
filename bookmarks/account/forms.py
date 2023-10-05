from django import forms


class LoginForm(forms.Form):
    """форма для входа в аккаунт"""

    username = forms.CharField(label="Имя пользователя")
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль")
