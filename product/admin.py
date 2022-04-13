from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models
from .models import (
    Category,
    Product,
    ProductImage,
)

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display       = ('name', 'slug', 'image', 'caption')
    list_display_links = ('name',)
    list_editable      = ('slug', 'image', 'caption',)
    search_fields      = ('name', 'slug', )
    ordering           = ('name', 'slug', )

    prepopulated_fields = {'slug' : ('name',)}

    fieldsets = (
        ('Category Info', {
            "fields": (
                'name', 'slug', 'image', 'caption',
            ),
        }),
    )    
admin.site.register(Category, CategoryAdmin)



class ProductImageAdmin(admin.TabularInline):
    model   = ProductImage
    extra   = 1
    max_num = 4

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin,]

    list_display       = ('pk', 'category', 'name', 'product_model', 'slug', 'guarentee', 'delivery_uzb', 'delivery_toshkent')
    list_display_links = ('pk', 'name',)
    list_editable      = ('category', 'slug', 'product_model', 'guarentee', 'delivery_uzb', 'delivery_toshkent')
    search_fields      = ('category', 'name', 'slug', 'product_model', 'guarentee', 'delivery_uzb', 'delivery_toshkent')
    ordering           = ('pk', 'category', 'name', 'slug', 'product_model', 'guarentee', 'delivery_uzb', 'delivery_toshkent')

    prepopulated_fields = {'slug' : ('product_model',)}

    fieldsets = (
        ('Category', {
            "fields": (
                'category',
            ),
        }),
        ('Proruct Info', {
            "fields": (
                'name', 'product_model', 'slug', 'description', 'guarentee', 'delivery_uzb', 'delivery_toshkent'
            ),
        }),
    )
    formfield_overrides = {
        models.TextField : {'widget' : TinyMCE}
    }
admin.site.register(Product, ProductAdmin)