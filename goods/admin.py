from django.contrib import admin
from goods.models import Categories, Products

# Регестрируем таблицу Category чтобы она была видна в админке
# и добавляем возможность редактировать поля slug в админке
@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}