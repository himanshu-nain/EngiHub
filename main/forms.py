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
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Book Title', 'class': 'form-control w-25'}))
    author = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Book Author', 'class': 'form-control w-25'}))
    desc = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Book Description', 'class': 'form-control w-25'}))

    class Meta:
        model = File
        fields = ['name', 'author', 'desc', 'file']
