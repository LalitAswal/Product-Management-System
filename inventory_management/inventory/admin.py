from django.contrib import admin
from .models import ProductMovement, Product, Location


admin.site.register(Product)
admin.site.register(ProductMovement)
admin.site.register(Location)
# Register your models here.
