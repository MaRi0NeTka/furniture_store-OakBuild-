from django.shortcuts import render


def login(request):
    context = {
        'title': 'Вход в систему',
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