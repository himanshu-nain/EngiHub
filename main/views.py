from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import logout
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.decorators import login_required
from .forms import UserForm, FileForm


def intro(request):
    return render(request, 'intro_templates/intro.html', {})


def _login_(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(request.POST.get('next',default = '/dashboard'))
            else:
                return render(request, 'login/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'login/login.html', {'error_message': 'Invalid Login Credentials'})

    return render(request, 'login/login.html', {})


@login_required
def _dash_(request):
    return render(request, 'dashboard/dashboard.html', {})


@login_required
def upload_file(request):
    form = FileForm(request.POST or None)
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/dashboard')

    return render(request, 'file/upload.html', {
        'form':form,
    })


def _logout_(request):
    logout(request)
    return redirect('/login')


def _register_(request):
    form = UserForm(request.POST or None)

    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        email = form.cleaned_data['email']
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/dashboard')
    context = {
        "form": form,
    }
    return render(request, 'login/register.html', context)

