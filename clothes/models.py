from django.db import models

class Clothing(models.Model):
    CATEGORY_CHOICES = [
        ('Tops', 'Tops'),
        ('Bottoms', 'Bottoms'),
        ('Dresses', 'Dresses'),
        ('Outerwear', 'Outerwear'),
        ('Accessories', 'Accessories'),
    ]

    name = models.CharField(max_length=255)
    producer = models.ForeignKey('producer.Producer', on_delete=models.CASCADE, related_name='clothing_items', null=True, blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    # image = models.ImageField(upload_to='clothes/', blank=True, null=True)
    # stock = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name