from django.db import models

# Create your models here.
class Food(models.Model):
    title = models.CharField(max_length = 60)
    price = models.IntegerField()
    recommend = models.BooleanField(default = False)
    description = models.TextField(null = True, blank = True)
    image_relative_url = models.CharField(max_length=50, null=True, blank=True)
    
class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2) 