from django.contrib import admin

from orders.models import Order
from users.models import User

class OrderInline(admin.TabularInline):
    model = Order
    extra = 0


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    search_fields = ['first_name', 'last_name', 'username']
    inlines = [OrderInline,]