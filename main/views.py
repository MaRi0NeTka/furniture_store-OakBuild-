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