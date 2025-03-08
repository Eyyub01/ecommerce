from django.contrib import admin
from .models import *

class ClothingAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'manufacturer', 'created_at', 'updated_at')
    list_filter = ('category', 'manufacturer', 'created_at')
    search_fields = ('name', 'category', 'manufacturer')
    ordering = ('-created_at',)
    fieldsets = (
        (None, {
            'fields': ('name', 'category', 'price', 'description', 'manufacturer')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(Clothing, ClothingAdmin)
