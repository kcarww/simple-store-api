from django.contrib import admin

from core.product.domain.product import Product

class ProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)
