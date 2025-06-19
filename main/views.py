from django import template
from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):  # Создаем класс для представления главной страницы
    template_name = 'main/index.html'  # Указываем шаблон для главной страницы


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # Получаем контекст из родительского класса
        context['title'] = 'OakBuild - Главная страница'  # Добавляем заголовок
        context['content'] = "Магазин Мебели и Декора"
        return context 
    

class AboutPageView(TemplateView):  # Создаем класс для представления страницы "О нас"
    template_name = 'main/about.html'  # Указываем шаблон для страницы "О нас"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'OakBuild - О нас'
        context['content'] = "О нашем магазине"
        context['text_on_page'] = """Добро пожаловать в House – ваш источник стильной и качественной мебели!
        У нас вы найдете современные и классические решения для дома и офиса.
        Комфорт, надежность и доступные цены – все для уюта вашего пространства. 🚪🛋✨"""
        return context

class DeliveryView(TemplateView):
    template_name = 'main/delivery.html'  # Указываем шаблон для страницы доставки

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'OakBuild - Доставка'
        context['content'] = "Доставка и оплата"
        context['text_on_page'] = """Мы предлагаем несколько способов доставки:
        1. Курьерская доставка по Киеву.
        2. Доставка Новой Почтой по всей Украине.
        3. Самовывоз из нашего магазина в Киеве."""
        return context
    
class ContactView(TemplateView):
    template_name = 'main/contact.html'  # Указываем шаблон для страницы контактов

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'OakBuild - Контакты'
        context['content'] = "Контактная информация"
        context['text_on_page'] = """г. Киев, ул. Героев ОУН, 12
        Телефоны:
        +38 (050) 123-45-67 — Viber / Telegram
        +38 (073) 234-56-78 — звонки

        Email:
        support@example.com

        Режим работы:
        Понедельник – Пятница: 10:00 – 18:00
        Суббота: 10:00 – 15:00
        Воскресенье: выходной"""
        return context


# def index(request):#делаем контролер и регестрируем его в urls.py
#     context = {
#         'title':'House - Главная страница',
#         'content':"Магазин Мебели и Декора",
#     }
#     return render(request, 'main/index.html', context=context) #передаем контекстные переменные в шаблон


# def about(request):#делаем контролер и регестрируем его в urls.py
#     context = {
#         'title':'House - О нас',
#         'content':"О нашем магазине",
#         'text_on_page': """Добро пожаловать в House – ваш источник стильной и качественной мебели!
#         У нас вы найдете современные и классические решения для дома и офиса.
#         Комфорт, надежность и доступные цены – все для уюта вашего пространства. 🚪🛋✨""",
#     }
    
#     return render(request, 'main/about.html', context = context)