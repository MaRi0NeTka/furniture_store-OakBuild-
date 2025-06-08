from django.contrib import admin

from orders.models import Order, OrderItem

class OrderTabularAdmin(admin.TabularInline):
    model = OrderItem
    extra = 0 #отвечает за количество пустых строк в форме
    fields = ('product', 'name', 'price', 'quantity', )
    search_fields = 'product', 'name'

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = 'product', 'name', 'price', 'quantity', 'order'
    search_fields = 'product', 'name', 'order__user__username', 'order'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('created_timestamp',)
    list_display = (
        'id',
        'phone_number',
        'user',
        'created_timestamp',
        'status',
        'is_paid',
        'payment_on_get',
        'requires_delivery'

        )
    search_fields = (
        'user__username', 'pk', 'phone_number')
    list_filter = (
        'status', 
        'is_paid', 
        'requires_delivery',
        'payment_on_get',
        'created_timestamp',
        )
    inlines = (OrderTabularAdmin,)