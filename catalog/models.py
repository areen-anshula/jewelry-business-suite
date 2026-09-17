from django.db import models
from customers.models import Customer


class Product(models.Model):

    class Category(models.TextChoices):
        RINGS = "RINGS", "Rings"
        NECKLACES = "NECKLACES", "Necklaces"
        EARRINGS = "EARRINGS", "Earrings"
        BRACELETS = "BRACELETS", "Bracelets"
        LOOSE_STONES = "LOOSE_STONES", "Loose stones"

    class Status(models.TextChoices):
        ACTIVE = "ACTIVE", "Active"
        INACTIVE = "INACTIVE", "Inactive"

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=Category.choices)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.INACTIVE)

    def __str__(self):
        return self.name


class ProductImage(models.Model):

    class ImageType(models.TextChoices):
        FRONT = "FRONT", "Front view"
        SIDE = "SIDE", "Side view"
        WORN = "WORN", "Worn view"
        CLOSE_UP = "CLOSE_UP", "Close-up"

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="products/")
    image_type = models.CharField(max_length=20,choices=ImageType.choices)

    def __str__(self):
        return f"{self.product.name} - {self.get_image_type_display()}"


class Stock(models.Model):

    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name="stock")
    stock_quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.product.name} - {self.stock_quantity}"


class CustomizationRequest(models.Model):

    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending"
        APPROVED = "APPROVED", "Approved"
        REJECTED = "REJECTED", "Rejected"

    customer = models.ForeignKey(Customer,on_delete=models.CASCADE, related_name="customization_requests")
    product = models.ForeignKey(Product,on_delete=models.CASCADE, related_name="customization_requests")
    request = models.TextField()
    status = models.CharField(max_length=20,choices=Status.choices, default=Status.PENDING)
    reviewed_at = models.DateTimeField(blank=True, null=True)
    owner_note = models.TextField(blank=True)

    def __str__(self):
        return f"{self.customer} - {self.product}"