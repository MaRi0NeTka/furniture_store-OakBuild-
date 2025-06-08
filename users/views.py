import re
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.db.models import Prefetch
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.urls import reverse

from carts.models import Cart
from orders.models import Order, OrderItem
from users.forms import UserLoginForm, UserRegisterForm, UserEditForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid(): # проверяем валидность формы, а именно, валидность введенных данных
            username = request.POST['username'] # получаем имя пользователя из формы
            password = request.POST['password'] # получаем пароль из формы
            user = auth.authenticate(username=username, password=password) # аутентифицируем пользователя
            
            ''''получаем session_key пользователя, чтобы подвязать его корзину(когда он был не авторизован)
               к сессионному ключу, чтобы потом не потерять корзину при авторизации'''
            session_key = request.session.session_key
            
            if user:
                auth.login(request, user)
                messages.success(request, f'Вы успешно вошли в систему как {username}')

                if session_key:
                    Cart.objects.filter(session_key=session_key).update(user=user) # обновляем корзину пользователя, если он был не авторизован
                    Cart.objects.update(session_key=None) # очищаем session_key пользователя, чтобы не было путаницы

                redirected_page = request.POST.get('next', None)
                if redirected_page and redirected_page != reverse('user:logout'):
                    """проверяем, если он пыттается зайти на профиль не авторизовавшись, то перенаправляем
                       его на страницу регистрации и после успешной регистрации перенаправляем на страницу профиля"""
                    return HttpResponseRedirect(request.POST.get('next'))# перенаправляем на /user/profile/
                
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm() # создаем пустую форму, если метод GET
    context = {
        'title': 'Вход в систему',
        'form': form,  # передаем форму в контекст
    }
    return render(request, 'users/login.html', context=context)


def registration(request):
    if request.method == "POST":
        form = UserRegisterForm(data=request.POST)  # создаем форму с данными из POST запроса
        if form.is_valid():
            form.save() # сохраняем форму в БД

            session_key = request.session.session_key

            user = form.instance  # получаем экземпляр формы
            auth.login(request, user)
            messages.success(request, f'Вы успешно зарегистрировались')
            
            if session_key:
                Cart.objects.filter(session_key=session_key).update(user=user)
                Cart.objects.update(session_key=None) # очищаем session_key пользователя, чтобы не было путаницы


            return HttpResponseRedirect(reverse('user:login')) # перенаправляем на страницу входа в систему
        
    else:
        form = UserRegisterForm() # создаем пустую форму, если метод GET
    context = {
        'title': 'Вход в систему',
        'form':form # передаем форму в контекст
    }
    return render(request, 'users/registration.html', context=context)


@login_required
def profile(request):
    if request.method == "POST":
        form = UserEditForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():            
            form.save()
            messages.success(request, f'Профиль успешно обновлен')
            return redirect('user:profile')  
        else:
            print("Форма невалидна:", form.errors)      
    else:
        form = UserEditForm(instance=request.user)

    orders = Order.objects.filter(user=request.user).prefetch_related(
        Prefetch('items', queryset=OrderItem.objects.select_related('product'))
    ).order_by('-id')
    context = {
        'title': 'Вход в систему',
        'form': form,
        'orders':orders,
    }
    return render(request, 'users/profile.html', context=context)


def user_cart(request):
    return render(request, 'users/user_cart.html')



@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, f'Вы вышли из системы')
    return redirect('main:index') # перенаправляем на главную страницу после выхода из системы