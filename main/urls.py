from django.urls import path

from main import views

app_name = 'main'  # пространство имен для приложения main

urlpatterns = [
    path('', views.HomePageView.as_view(), name='index'),#добавляем контролер, name - это имя маршрута для использования в шаблонах
    path('about/', views.AboutPageView.as_view(), name='about'),#добавляем контролер, name - это имя маршрута для использования в шаблонах
    path('delivery/', views.DeliveryView.as_view(), name='delivery'),#добавляем контролер, name - это имя маршрута для использования в шаблонах
    path('contact/', views.ContactView.as_view(), name='contact'),#добавляем контролер, name - это имя маршрута для использования в шаблонах
]