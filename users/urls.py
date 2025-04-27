from django.urls import path

from users import views

app_name = 'users'  # пространство имен для приложения users

urlpatterns = [
    path('login/', views.login, name='login'),  # страница входа в систему
    path('registration/', views.registration, name='registration'),  # страница регистрации
    path('profile/', views.profile, name='profile'),  # страница профиля
    path('logout/', views.logout, name='logout'),  # страница выхода из системы

]