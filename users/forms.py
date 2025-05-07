"""Описывает формы для работы с пользователями.
Также будет содержать проверки на уникальность и валидность данных.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from users.models import User

class UserLoginForm(AuthenticationForm):
    """Форма для входа в систему."""
    class Meta:
        model = User
        fields = ('username', 'password')

    # username = forms.CharField()
    # password = forms.CharField()  Не использовал html атрибуты здесь, а прописывал их в шаблоне добавляя - name="password" id="id_password"

    #              OR

    # username = forms.CharField(     пример использования атрибутов в форме
    #     label='Имя пользователя',
    #     widget=forms.TextInput(attrs={
    #         "autofocus": True,
    #         'class':'form-control',
    #         'placeholder':'Введите ваше имя пользователя',
    #         }),
    # )
    # password = forms.CharField(
    #     label='Пароль',
    #     widget=forms.PasswordInput(attrs={
    #         "autocomplete": "current-password",
    #         'class':'form-control',
    #         'placeholder':'Введите ваш пароль'
    #         }),
    # )


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ( #указываем поля, которые хотим использовать в форме
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
        )

    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()