from django.contrib import admin
from .models import Clothing

@admin.register(Clothing)
class ClothingAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'producer', 'is_active', 'created_at', 'expires_at')  # Added 'is_active' and 'expires_at'
    list_filter = ('category', 'producer', 'is_active', 'created_at')  # Added 'is_active' filter
    search_fields = ('name', 'category', 'producer__name', 'description')  # Added 'description' to search fields
    ordering = ('-created_at',)  # Default ordering by newest first
    list_editable = ('is_active',)  # Allow 'is_active' to be edited directly in the list view
    date_hierarchy = 'created_at'  # Adds a date-based drilldown navigation

    readonly_fields = ('created_at', 'updated_at')  # Mark non-editable fields as read-only

    fieldsets = (
        (None, {
            'fields': ('name', 'category', 'price', 'description', 'producer', 'is_active')  # Editable fields only
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at', 'expires_at'),  # Read-only fields
            'classes': ('collapse',)  # Collapsible section for timestamps
        }),
    )