from django.contrib import admin
from .models import (Profile,Products,Cart,CartItem,Payment,ProductHistory,Comment,Rate)

admin.site.register(Profile)
admin.site.register(Products)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Payment)
admin.site.register(ProductHistory)
admin.site.register(Comment)
admin.site.register(Rate)