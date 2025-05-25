from django.contrib import admin

from carts.models import Cart


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'product__name', 'quantity']
    search_fields = ['user__first_name', 'user__last_name', 'product__name']
    list_filter = ['user', 'product__name']