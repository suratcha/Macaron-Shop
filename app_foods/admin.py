from django.contrib import admin

from app_foods.models import Food, Order, OrderItem

# Register your models here.
class FoodAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'recommend']
    search_fields = ['title']
    list_filter = ['recommend']
    
admin.site.register(Food, FoodAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)