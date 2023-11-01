from django.contrib import admin
from . models import *
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title','author','price','slug', 'in_stock', 'created_on', 'updated_on')
    list_filter = ('in_stock', 'is_active')
    list_editable = ('price', 'in_stock')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Product,ProductAdmin)
