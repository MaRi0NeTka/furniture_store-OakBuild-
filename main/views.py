from django.shortcuts import render
from goods.models import Categories
# Create your views here.
def index(request):#делаем контролер и регестрируем его в urls.py
    context = {
        'title':'House - Главная страница',
        'content':"Магазин Мебели и Декора",
    }
    return render(request, 'main/index.html', context=context) #передаем контекстные переменные в шаблон


def about(request):#делаем контролер и регестрируем его в urls.py
    context = {
        'title':'House - О нас',
        'content':"О нашем магазине",
        'text_on_page': """Добро пожаловать в House – ваш источник стильной и качественной мебели!
        У нас вы найдете современные и классические решения для дома и офиса.
        Комфорт, надежность и доступные цены – все для уюта вашего пространства. 🚪🛋✨""",
    }
    
    return render(request, 'main/about.html', context = context)