from django.contrib import admin
from .models import Clothing

class ClothingAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'producer', 'created_at', 'updated_at')
    list_filter = ('category', 'producer', 'created_at')
    search_fields = ('name', 'category', 'producer__name')
    ordering = ('-created_at',)
    fieldsets = (
        (None, {
            'fields': ('name', 'category', 'price', 'description', 'producer')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(Clothing, ClothingAdmin)