from django.contrib import admin
from goods.models import Categories, Products


# Регестрируем таблицу Category чтобы она была видна в админке
# и добавляем возможность редактировать поля slug в админке
@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name",]


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    # Отображение полей в админке - навпротив товара отображается параметры ниже
    list_display = ["name", "quantity", "price", "discount"]
    list_editable = [
        "discount"
    ]  # поля, которые можно редактировать в админке без перехода в редактирование товара
    search_fields = [
        "name",
        "description",
    ]  # поля, по которым можно искать товары в админке
    list_filter = ["category"]  # фильтр по заданым атрибутам товаров в админке
    fields = [ # поля, которые будут отображаться при редактировании товара
        "name",
        "slug",
        "category",
        "description",
        ("quantity","price"),  # кортеж для отображения полей в одной строке
        "discount",
        "image",
    ]
