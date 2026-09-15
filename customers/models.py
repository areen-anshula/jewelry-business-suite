import uuid
from django.core.validators import RegexValidator
from django.db import models
from accounts.models import User

phone_validator = RegexValidator(
    regex=r"^\+?[0-9]{9,15}$",
    message="Enter a valid phone number, e.g. +94771234567",
)


class Country(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    iso_code = models.CharField(max_length=3, unique=True, help_text="ISO 3166-1 alpha-2/3 code, e.g. LK")

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.name


class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="customer_profile")

    phone_number = models.CharField(max_length=15, validators=[phone_validator])

    notes = models.TextField(blank=True)  

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [models.Index(fields=["phone_number"])]

    def __str__(self):
        return f"{self.user.email} ({self.phone_number})"


class Address(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="addresses")
    country = models.ForeignKey(Country, on_delete=models.PROTECT, related_name="addresses")

    label = models.CharField(max_length=50)  
    recipient_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, validators=[phone_validator])

    address_line_1 = models.CharField(max_length=150)
    address_line_2 = models.CharField(max_length=150, blank=True)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)

    is_default = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-is_default", "-created_at"]
        constraints = [
            models.UniqueConstraint(
                fields=["customer"],
                condition=models.Q(is_default=True),
                name="unique_default_address_per_customer",
            )
        ]

    def __str__(self):
        return f"{self.recipient_name} - {self.label}"