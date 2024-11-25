from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cart(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="customer")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.customer}'


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cart_items")
    title = models.CharField(max_length=300)
    quantity = models.IntegerField(default=1)
    price = models.FloatField()
    image = models.URLField()

    def __str__(self) -> str:
        return self.title