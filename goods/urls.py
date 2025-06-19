from django.urls import path
from goods import views

app_name = 'goods'  # пространство имен для приложения goods

urlpatterns = [
    path('search/', views.CatalogView.as_view(), name='search'),# главная страница каталога товаров
    path('<slug:category_slug>/', views.CatalogView.as_view(), name='index'),# главная страница каталога товаров
    path('product/<slug:product_slug>/',views.ProductView.as_view(), name='product'),# отлавливает обращение по slug
]
