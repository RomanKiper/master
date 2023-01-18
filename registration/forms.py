from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import CharField, TextInput, PasswordInput, EmailInput, EmailField


class RegisterForm(UserCreationForm):
    username = CharField(
        max_length=150,
        widget=TextInput(
            attrs={
                'class': 'input100',
                'name': 'username',
                'placeholder': 'Введите логин',
                'style': 'width: 25rem'
            }
        )
    )
    email = EmailField(
        widget=EmailInput(
            attrs={
                'class': 'input100',
                'name': 'email',
                'placeholder': 'Введите адрес электронной почты',
                'style': 'width: 25rem'
            }
        )
    )
    password1 = CharField(
        min_length=8,
        widget=PasswordInput(
            attrs={
                'class': 'input100',
                'name': 'password1',
                'placeholder': 'Введите пароль',
                'style': 'width: 25rem'
            }
        )

    )
    password2 = CharField(
        min_length=8,
        widget=PasswordInput(
            attrs={
                'class': 'input100',
                'name': 'password2',
                'placeholder': 'Повторите пароль',
                'style': 'width: 25rem'
            }
        )

    )



    class Meta:
        fields = ('username', 'email', 'password1', 'password2')
        model = User


class Loginform(AuthenticationForm):
    username = CharField(
        max_length=150,
        widget=TextInput(
            attrs={
                'class': 'input100',
                'name': 'username',
                'placeholder': 'Введите логин',
                'style': 'width: 25rem'
            }
        )
    )
    password = CharField(
        min_length=8,
        widget=PasswordInput(
            attrs={
                'class': 'input100',
                'name': 'password',
                'placeholder': 'Введите пароль',
                'style': 'width: 25rem'
            }
        )

    )



