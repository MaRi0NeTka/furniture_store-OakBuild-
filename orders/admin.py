from django.contrib import admin

from orders.models import Order, OrderItem

admin.site.register(OrderItem)
admin.site.register(Order)

# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     search_fields = ['user__username', 'pk', 'phone_number']
