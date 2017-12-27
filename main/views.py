from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, update_session_auth_hash
import os
from django.conf import settings
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth import logout as outlog
from django.contrib.auth.decorators import login_required
from .forms import UserForm, FileForm, FormChangePassword

from .models import File


def intro(request):
    try:
        if request.user.is_authenticated:
            return redirect('/dashboard')
        return render(request, 'intro_templates/intro.html', {})
    except:
        import sys
        print(str(sys.exc_info()))
        return render(request, 'intro_templates/intro.html', {})


def _login_(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                if request.POST['next'] == '':
                    return redirect('/dashboard')
                return redirect(request.POST['next'])
            else:
                return render(request, 'login/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'login/login.html', {'error_message': 'Invalid Login Credentials'})

    return render(request, 'login/login.html', {})


@login_required
def _dash_(request):

    try:
        files = File.objects.all()
        return render(request, 'dashboard/dashboard.html', {'files': files})
    except:
        import sys
        print(str(sys.exc_info()))
        files = []
        return render(request, 'dashboard/dashboard.html', {'files': files})


@login_required
def _my_uploads_(request):
    user_id = request.user.id
    files = File.objects.filter(uploader_id=user_id)
    return render(request, 'dashboard/dashboard.html', {'files': files})


@login_required
def upload_file(request):
    form = FileForm(request.POST or None)
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.uploader = request.user
            form.save()
            return redirect('/dashboard')

    return render(request, 'file/upload.html', {
        'form': form,
    })


def download_file(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404


def delete_file(request, id):
    try:
        File.objects.get(pk=id).delete()
    except FileNotFoundError:
        return Http404

    return HttpResponseRedirect('/dashboard')


def like(request, id):
    obj = File.objects.get(pk=id)
    obj.uplike()
    obj.save()
    return HttpResponseRedirect('/dashboard')


def dislike(request, id):
    obj = File.objects.get(pk=id)
    obj.downlike()
    obj.save()
    return HttpResponseRedirect('/dashboard')


def _logout_(request):
    outlog(request)
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


def file_details(request, id):
    try:
        file = File.objects.get(pk=id)

        return render(request, 'file/detail.html', {'file':file})
    except FileNotFoundError:
        return Http404


@login_required
def my_account(request):

    return render(request, 'dashboard/profile.html',{})


def change_password(request):
    if request.method == 'POST':
        form = FormChangePassword(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = FormChangePassword(request.user)
    return render(request, 'accounts/change_password.html', {
        'form': form
    })


@login_required
def change_email(request):
    if request.method == 'POST':
        newEmail = request.POST['newEmail']
        user = User.objects.get(username = request.user.username)
        user.email = newEmail
        user.save()
        return redirect('/account')

    else:
        return render(request, 'accounts/change_email.html', {})
