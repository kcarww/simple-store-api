from django.db import models
from uuid import uuid4

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    active = models.BooleanField(default=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"<ProductModel> id: {self.id}, name: {self.name}, price: {self.price}, stock: {self.stock}, active: {self.active}, description: {self.description}, created_at: {self.created_at}, updated_at: {self.updated_at}"