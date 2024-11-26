from django.contrib import admin
from .models import Product,ProductMedia







@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','price','description'] 
    list_editable = ['price']
    list_per_page = 20
   
    
    
# # Register your models here.
# @admin.register(Collection)
# class CollectionAdmin(admin.ModelAdmin):
#     inlines = [CollectionInline]
#     exclude = ['product']
#     list_display = ['id','title']
#     list_per_page = 20
