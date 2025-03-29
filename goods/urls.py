from django.urls import path
from goods import views

app_name = 'goods'  # пространство имен для приложения goods

urlpatterns = [
    path('', views.catalog, name='index'),# главная страница каталога товаров
    path('product/',views.product, name='product'),# страница товара
]
