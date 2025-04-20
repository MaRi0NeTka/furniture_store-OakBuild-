from django.urls import path
from goods import views

app_name = 'goods'  # пространство имен для приложения goods

urlpatterns = [
    path('<slug:category_slug>/', views.catalog, name='index'),# главная страница каталога товаров
    path('product/<int:product_id>/',views.product, name='product'),# отлавливает обращение по id(нужно записывать первым чтобы не было конфликта с product_slug)
    path('product/<slug:product_slug>/',views.product, name='product'),# отлавливает обращение по slug
]
