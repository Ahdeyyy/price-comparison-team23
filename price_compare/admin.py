from django.contrib import admin
from .models import Product,Comment
# Register your models here.

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display =  ('username','product','created','active')
    list_filter = ('active' , 'created')
    search_fields = ('username', 'product','body')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    search_fields = ('name','id')
