from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import auth, messages
from django.db.models import Prefetch
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView

from carts.models import Cart
from orders.models import Order, OrderItem
from users.forms import UserLoginForm, UserRegisterForm, UserEditForm


class UserLoginView(LoginView):
    template_name = 'users/login.html'  # указываем шаблон для страницы входа
    form_class = UserLoginForm

    def form_valid(self, form):
        session_key = self.request.session.session_key
        user = form.get_user()
        if user:
            auth.login(self.request, user)            
            if session_key:
                Cart.objects.filter(session_key=session_key).update(user=user)
                messages.success(self.request, f'Вы успешно вошли в систему как {user.username}')
                return HttpResponseRedirect(reverse('main:index'))

    def get_success_url(self):
        redirected_page = self.request.POST.get('next', None)
        if redirected_page and redirected_page != reverse('user:logout'):
            """проверяем, если он пыттается зайти на профиль не авторизовавшись, то перенаправляем
               его на страницу регистрации и после успешной регистрации перенаправляем на страницу профиля"""
            return redirected_page  # перенаправляем на страницу, на которую он хотел попасть
        # если redirected_page не указан, то перенаправляем на главную страницу
        return reverse_lazy('main:index')  # перенаправляем на главную страницу после успешного входа
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Вход в систему'
        return context
    

class UserRegisterView(CreateView):
    template_name = 'users/registration.html'  # указываем шаблон для страницы регистрации
    form_class = UserRegisterForm  # указываем форму для регистрации
    success_url = reverse_lazy('user:profile')

    def form_valid(self, form):
        session_key = self.request.session.session_key
        user = form.instance
        if user:
            form.save()
            auth.login(self.request, user)
            if session_key:
                Cart.objects.filter(session_key=session_key).update(user=user)
                messages.success(self.request, f'Вы успешно зарегистрировались')
            return HttpResponseRedirect(self.success_url)  # перенаправляем на страницу профиля после успешной регистрации
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        context['form'] = self.get_form()  # передаем форму в контекст
        return context


class UserProfileEditView(LoginRequiredMixin, UpdateView):
    template_name = 'users/profile.html'  # указываем шаблон для страницы профиля
    form_class = UserEditForm  # указываем форму для редактирования профиля
    success_url = reverse_lazy('user:profile')

    def get_object(self, queryset = None):
        return self.request.user  # получаем текущего пользователя для редактирования его профиля

    def form_invalid(self, form):
        messages.error(self.request, 'Ошибка при обновлении профиля')
        return super().form_invalid(form)

    def form_valid(self, form):        
        if self.request.POST.get('default_avatar') == 'on':
            form.instance.image = None  # если галочка "Использовать аватар по умолчанию" установлена, то удаляем аватар пользователя
        messages.success(self.request, 'Профиль успешно обновлен')
        return super().form_valid(form)  # перенаправляем на страницу профиля после успешного редактирования
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Профиль'
        context['orders'] = Order.objects.filter(user=self.request.user).prefetch_related(
            Prefetch('items', queryset=OrderItem.objects.select_related('product'))
        ).order_by('-id')
        return context
    

class UserCartView(TemplateView):
    template_name = 'users/user_cart.html'  # указываем шаблон для страницы корзины пользователя

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Корзина'

# def login(request):
#     if request.method == 'POST':
#         form = UserLoginForm(request, data=request.POST)
#         if form.is_valid(): # проверяем валидность формы, а именно, валидность введенных данных
#             username = request.POST['username'] # получаем имя пользователя из формы
#             password = request.POST['password'] # получаем пароль из формы
#             user = auth.authenticate(username=username, password=password) # аутентифицируем пользователя
            
#             ''''получаем session_key пользователя, чтобы подвязать его корзину(когда он был не авторизован)
#                к сессионному ключу, чтобы потом не потерять корзину при авторизации'''
#             session_key = request.session.session_key
            
#             if user:
#                 auth.login(request, user)
#                 messages.success(request, f'Вы успешно вошли в систему как {username}')

#                 if session_key:
#                     Cart.objects.filter(session_key=session_key).update(user=user) # обновляем корзину пользователя, если он был не авторизован
#                     Cart.objects.update(session_key=None) # очищаем session_key пользователя, чтобы не было путаницы

#                 redirected_page = request.POST.get('next', None)
#                 if redirected_page and redirected_page != reverse('user:logout'):
#                     """проверяем, если он пыттается зайти на профиль не авторизовавшись, то перенаправляем
#                        его на страницу регистрации и после успешной регистрации перенаправляем на страницу профиля"""
#                     return HttpResponseRedirect(request.POST.get('next'))# перенаправляем на /user/profile/
                
#                 return HttpResponseRedirect(reverse('main:index'))
#     else:
#         form = UserLoginForm() # создаем пустую форму, если метод GET
#     context = {
#         'title': 'Вход в систему',
#         'form': form,  # передаем форму в контекст
#     }
#     return render(request, 'users/login.html', context=context)


# def registration(request):
#     if request.method == "POST":
#         form = UserRegisterForm(data=request.POST)  # создаем форму с данными из POST запроса
#         if form.is_valid():
#             form.save() # сохраняем форму в БД

#             session_key = request.session.session_key

#             user = form.instance  # получаем экземпляр формы
#             auth.login(request, user)
#             messages.success(request, f'Вы успешно зарегистрировались')
            
#             if session_key:
#                 Cart.objects.filter(session_key=session_key).update(user=user)
#                 Cart.objects.update(session_key=None) # очищаем session_key пользователя, чтобы не было путаницы


#             return HttpResponseRedirect(reverse('user:login')) # перенаправляем на страницу входа в систему
        
#     else:
#         form = UserRegisterForm() # создаем пустую форму, если метод GET
#     context = {
#         'title': 'Вход в систему',
#         'form':form # передаем форму в контекст
#     }
#     return render(request, 'users/registration.html', context=context)


# @login_required
# def profile(request):
#     if request.method == "POST":
#         form = UserEditForm(data=request.POST, instance=request.user, files=request.FILES)
#         if form.is_valid():            
#             form.save()
#             messages.success(request, f'Профиль успешно обновлен')
#             return redirect('user:profile')  
#         else:
#             print("Форма невалидна:", form.errors)      
#     else:
#         form = UserEditForm(instance=request.user)

#     orders = Order.objects.filter(user=request.user).prefetch_related(
#         Prefetch('items', queryset=OrderItem.objects.select_related('product'))
#     ).order_by('-id')
#     context = {
#         'title': 'Вход в систему',
#         'form': form,
#         'orders':orders,
#     }
#     return render(request, 'users/profile.html', context=context)


# def user_cart(request):
#     return render(request, 'users/user_cart.html')



@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, f'Вы вышли из системы')
    return redirect('main:index') # перенаправляем на главную страницу после выхода из системы