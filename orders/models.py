from django.db import models
from customers.models import Customer, Address
from catalog.models import Product
import uuid


class Order(models.Model):

    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending"
        CONFIRMED = "CONFIRMED", "Confirmed"
        PACKAGING = "PACKAGING", "Packaging"
        SHIPPED = "SHIPPED", "Shipped"
        DELIVERED = "DELIVERED", "Delivered"
        CANCELLED = "CANCELLED", "Cancelled"
        REJECTED = "REJECTED", "Rejected"
        RETURNED = "RETURNED", "Returned"
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)    
    customer = models.ForeignKey(Customer,on_delete=models.PROTECT,related_name="orders_of_customer")
    shipping_address = models.ForeignKey(Address,on_delete=models.PROTECT,related_name="orders")
    status = models.CharField(max_length=20,choices=Status.choices,default=Status.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.id}"


class OrderItem(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name="items")
    product = models.ForeignKey(Product,on_delete=models.PROTECT,related_name="order_items")
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"

    @property
    def subtotal(self):
        return self.quantity * self.unit_price