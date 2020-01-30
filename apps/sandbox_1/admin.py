from django.contrib import admin
from .models import Product, HistoryProductPrice


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')


class HistoryProductPriceAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'price', 'date')


admin.site.register(Product, ProductAdmin)
admin.site.register(HistoryProductPrice, HistoryProductPriceAdmin)

