from django.contrib import admin
from .models import Categories, Clients, Products, Orders, Subcategories

admin.site.register(Clients)
admin.site.register(Categories)
admin.site.register(Products)
admin.site.register(Orders)
admin.site.register(Subcategories)
