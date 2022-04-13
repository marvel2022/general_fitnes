from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models

from .models import (
    HomePicture, 
    FeedBack, 
    About,
)

# Register your models here.

class HomePctureAdmin(admin.ModelAdmin):
    list_display       = ('pk', 'image', 'caption', 'active',)
    list_display_links = ('pk',)
    search_fields      = ('pk', 'image', 'caption')
    list_editable      = ('image', 'caption', 'active',)
    ordering           = ('pk', 'caption', 'active',)

    fieldsets=(
        ('Assosiy rasm', {
            'fields' : (
                'image', 'caption',
            )
        }),
    )
admin.site.register(HomePicture, HomePctureAdmin)


class AboutAdmin(admin.ModelAdmin):
    list_display=('pk', 'image', 'caption', 'active', 'about_text')
    list_display_links=('pk',)
    list_editable=('image', 'caption', 'active', 'about_text')
    search_fields=('pk', 'image', 'caption',)
    ordering=('pk', 'image', 'caption', 'active',)

    fieldsets = (
        ('Firma yoki korxona haqida ma\'lumot', {
            'fields': (
                'image', 'caption', 'about_text',
            )
        }),
    )

    formfield_overrides = {
        models.TextField : {'widget': TinyMCE }
    }
admin.site.register(About, AboutAdmin)


class FeedBackAdmin(admin.ModelAdmin):
    list_display=('pk', 'name', 'phonenumber', 'message')
    list_display_links=('pk', 'name', 'phonenumber',)
    # list_editable=()
    search_fields=('pk', 'name', 'phonenumber',)
    ordering=('pk', 'name', 'phonenumber',)

    fieldsets=(
        ('Feedback', {
            'fields': (
                'name', 'phonenumber', 'message',
            )
        }),
    )
admin.site.register(FeedBack, FeedBackAdmin)