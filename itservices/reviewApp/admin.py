from django.contrib import admin
from .models import Product, Review, Error

admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Error)