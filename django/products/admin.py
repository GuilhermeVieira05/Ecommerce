from django.contrib import admin
from products.models import Product, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'stock')
    search_fields = ('name',)
    list_filter = ('price', 'stock')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)