from django.urls import path
from goods import views

app_name = 'goods'  # пространство имен для приложения goods

urlpatterns = [
    path('search/', views.catalog, name='search'),# главная страница каталога товаров
    path('<slug:category_slug>/', views.catalog, name='index'),# главная страница каталога товаров
    path('product/<slug:product_slug>/',views.product, name='product'),# отлавливает обращение по slug
]
