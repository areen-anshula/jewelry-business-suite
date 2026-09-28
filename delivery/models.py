from django.db import models
from customers.models import Customer, Address
from catalog.models import Product
import uuid

from orders.models import Order

class Delivery(models.Model):
    class Method(models.TextChoices):
        CASH_ON_DELIVERY = "CASH_ON_DELIVERY", "Cash on delivery"
        CARD_PAYMENT = "CARD_PAYMENT", "Card payment"

    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending"
        PROCESSING = "PROCESSING", "Processing"
        SHIPPED = "SHIPPED", "Shipped"
        DELIVERED = "DELIVERED", "Delivered"
        FAILED = "FAILED", "Failed"
        RETURNED = "RETURNED", "Returned"
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)    
    order = models.OneToOneField(Order,on_delete=models.CASCADE,related_name="delivery")
    method = models.CharField(max_length=20,choices=Method.choices)
    status = models.CharField(max_length=20,choices=Status.choices,default=Status.PENDING)
    tracking_number = models.CharField(max_length=100,blank=True)
    shipped_at = models.DateTimeField(blank=True,null=True)
    delivered_at = models.DateTimeField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Delivery for Order {self.order.id}"