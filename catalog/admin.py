from django.contrib import admin
from catalog.models import Product, ProductImage, Stock, CustomizationRequest

admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Stock)
admin.site.register(CustomizationRequest)