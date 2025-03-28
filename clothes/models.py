from datetime import timedelta
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Clothing(models.Model):
    CATEGORY_CHOICES = [
        ('Tops', 'Tops'),
        ('Bottoms', 'Bottoms'),
        ('Dresses', 'Dresses'),
        ('Outerwear', 'Outerwear'),
        ('Accessories', 'Accessories'),
    ]

    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='clothing_items', null=True, blank=True)
    producer = models.ForeignKey('producer.Producer', on_delete=models.CASCADE, related_name='clothing_items', null=True, blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    # image = models.ImageField(upload_to='clothes/', blank=True, null=True)
    # stock = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    expires_at = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.expires_at:
            if not self.pk:  
                self.expires_at = timezone.now() + timedelta(days=30)  # Use django.utils.timezone
            else:  
                self.expires_at = self.created_at + timedelta(days=30)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} - {self.producer}'