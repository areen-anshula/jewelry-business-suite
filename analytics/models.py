from django.db import models
import uuid
from catalog.models import Product
from customers.models import Customer


class Event(models.Model):

    class EventType(models.TextChoices):
        PRODUCT_VIEW = "PRODUCT_VIEW", "Product view"
        PRODUCT_CLICK = "PRODUCT_CLICK", "Product click"
        ADD_TO_CART = "ADD_TO_CART", "Add to cart"
        PURCHASE = "PURCHASE", "Purchase"
        CUSTOMIZATION_REQUEST = "CUSTOMIZATION_REQUEST", "Customization request"

    class Source(models.TextChoices):
        WEBSITE = "WEBSITE", "Website"
        INSTAGRAM = "INSTAGRAM", "Instagram"
        FACEBOOK = "FACEBOOK", "Facebook"
        TIKTOK = "TIKTOK", "TikTok"
        WHATSAPP = "WHATSAPP", "WhatsApp"
        MESSENGER = "MESSENGER", "Messenger"
        GOOGLE = "GOOGLE", "Google"
        DIRECT = "DIRECT", "Direct"
        OTHER = "OTHER", "Other"
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    event_type = models.CharField(max_length=30,choices=EventType.choices)
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,blank=True,related_name="analytics_events")
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,blank=True,related_name="analytics_events")
    source = models.CharField(max_length=20,choices=Source.choices,default=Source.DIRECT)
    session_id = models.UUIDField(default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_event_type_display()} - {self.created_at}"