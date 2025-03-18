from django.db import models

class Producer(models.Model):
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=128, null=True, blank=True)

    def __str__(self):
        return self.name