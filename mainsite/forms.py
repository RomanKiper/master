from django.forms import ModelForm, EmailField, CharField, TextInput, EmailInput, Textarea, Form


from .models import Contact, EmailBase


class ContactForm(ModelForm):
    name = CharField(
        widget=TextInput(
            attrs={
                'class': 'form-control',
                'id': 'name',
                'placeholder': "Имя",

            }
        ),
        max_length=64
    )
    phone = CharField(
        widget=TextInput(
            attrs={
                'class': 'form-control',
                'id': 'phone',
                'placeholder': 'Номер телефона'
            }
        ),
        max_length=64
    )
    email = EmailField(
        widget=EmailInput(
            attrs={
                'class': 'form-control',
                'id': 'email',
                'placeholder': 'Эл.почта'
            }
        ),
        max_length=254
    )
    message = CharField(
        widget=Textarea(
            attrs={
                'class': 'form-control',
                'id': 'message',
                'placeholder': 'Напишите сообщение',
                'style': 'height: 7rem'
            }
        ),
        max_length=1024
    )

    class Meta:
        model = Contact
        fields = ('name', 'email', 'message', 'phone')


class EmailBaseForm(ModelForm):
    email = EmailField(
        widget=EmailInput(
            attrs={
                'class': 'form-control',
                'id': 'email',
                'placeholder': 'Email'
            }
        ),
        max_length=254
    )

    class Meta:
        model = EmailBase
        fields = ('email',)



