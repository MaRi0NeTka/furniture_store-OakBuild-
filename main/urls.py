from django.urls import path

from main import views

app_name = 'main'  # пространство имен для приложения main

urlpatterns = [
    path('', views.index, name='index'),#добавляем контролер, name - это имя маршрута для использования в шаблонах
    path('about/', views.about, name='about'),#добавляем контролер, name - это имя маршрута для использования в шаблонах
]