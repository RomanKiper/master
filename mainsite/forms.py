from django.forms import ModelForm, EmailField, CharField, TextInput, EmailInput, Textarea, Form

from .models import Contact


class ContactForm(ModelForm):
    name = CharField(
        widget=TextInput(
            attrs={
                'class': 'form-control',
                'id': 'name',
                'placeholder': "Name",

            }
        ),
        max_length=64
    )
    phone = CharField(
        widget=TextInput(
            attrs={
                'class': 'form-control',
                'id': 'phone',
                'placeholder': 'Phone'
            }
        ),
        max_length=64
    )
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
    message = CharField(
        widget=Textarea(
            attrs={
                'class': 'form-control',
                'id': 'message',
                'placeholder': 'Message',
                'style': 'height: 7rem'
            }
        ),
        max_length=1024
    )

    class Meta:
        model = Contact
        fields = ('name', 'email', 'message', 'phone')


class Myform(Form):
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
    phone = CharField(
        widget=TextInput(
            attrs={
                'class': 'form-control',
                'id': 'phone',
                'placeholder': 'Phone'
            }
        ),
        max_length=64
    )
