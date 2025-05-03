from email.policy import HTTP
from urllib.parse import uses_relative
from django.contrib import auth
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from users.forms import UserLoginForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid(): # проверяем валидность формы, а именно, валидность введенных данных
            username = request.POST['username'] # получаем имя пользователя из формы
            password = request.POST['password'] # получаем пароль из формы
            user = auth.authenticate(username=username, password=password) # аутентифицируем пользователя
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm() # создаем пустую форму, если метод GET
    context = {
        'title': 'Вход в систему',
        'form': form,  # передаем форму в контекст
    }
    return render(request, 'users/login.html', context=context)


def registration(request):
    context = {
        'title': 'Вход в систему',
    }
    return render(request, 'users/registration.html', context=context)


def profile(request):
    context = {
        'title': 'Вход в систему',
    }
    return render(request, 'users/profile.html', context=context)


def logout(request):
    ...