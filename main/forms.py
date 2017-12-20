from django.contrib.auth.models import User
from django import forms
from .models import File
from django.conf import settings
from django.core.exceptions import ValidationError


class UserForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']


class FileForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'mdl-textfield__input'}))
    author = forms.CharField(widget=forms.TextInput(attrs={'class': 'mdl-textfield__input'}))
    desc = forms.CharField(widget=forms.Textarea(attrs={'class': 'mdl-textfield__input','rows':'3'}), label='Description')

    class Meta:
        model = File
        fields = ['name', 'author', 'desc', 'file']

    def clean_file(self):
        file = self.cleaned_data.get('file', False)
        if file:

            # type = file.content_type.split('/')[0]

            if file._size > settings.MAX_UPLOAD_SIZE:
                raise ValidationError("File size too large. Max size is 100 MB")
            return file
        else:
            raise ValidationError("Could not read uploaded file")


