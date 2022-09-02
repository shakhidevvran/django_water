from django.contrib import admin
from .models import Client, Order

# Register your models here.
admin.site.register(Client)

class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ["name", 'contacts', 'created_at']

admin.site.register(Order, OrderAdmin)


