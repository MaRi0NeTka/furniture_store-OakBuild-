from django.urls import path

from users import views

app_name = 'user'  # пространство имен для приложения users

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),  # страница входа в систему
    path('registration/', views.UserRegisterView.as_view(), name='registration'),  # страница регистрации
    path('profile/', views.UserProfileEditView.as_view(), name='profile'),  # страница профиля
    path('user-cart/', views.UserCartView.as_view(), name='user_cart'),  # страница корзины пользователя
    path('logout/', views.logout, name='logout'),  # страница выхода из системы

]