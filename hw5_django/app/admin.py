from django.contrib import admin
from .models import Product
from app_2.models import Post

admin.site.register(Product)
admin.site.register(Post)