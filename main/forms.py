from django.contrib.auth.models import User
from django import forms
from .models import File


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
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name', 'class': 'mdl-textfield__input'}))
    author = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Author', 'class': 'mdl-textfield__input'}))
    desc = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Description', 'class': 'mdl-textfield__input'}))

    class Meta:
        model = File
        fields = ['name', 'author', 'desc', 'file']
