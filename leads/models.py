from django.db import models
import uuid
from customers.models import Customer


class Lead(models.Model):

    class Source(models.TextChoices):
        WEBSITE = "WEBSITE", "Website"
        INSTAGRAM = "INSTAGRAM", "Instagram"
        FACEBOOK = "FACEBOOK", "Facebook"
        TIKTOK = "TIKTOK", "TikTok"
        WHATSAPP = "WHATSAPP", "WhatsApp"
        MESSENGER = "MESSENGER", "Messenger"
        PHONE = "PHONE", "Phone"
        GOOGLE = "GOOGLE", "Google"
        OTHER = "OTHER", "Other"

    class Status(models.TextChoices):
        NEW = "NEW", "New"
        CONTACTED = "CONTACTED", "Contacted"
        INTERESTED = "INTERESTED", "Interested"
        NEGOTIATING = "NEGOTIATING", "Negotiating"
        CONVERTED = "CONVERTED", "Converted"
        LOST = "LOST", "Lost"
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)    
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,blank=True,related_name="leads")
    name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=20,blank=True)
    email = models.EmailField(blank=True)
    source = models.CharField(max_length=20,choices=Source.choices)
    status = models.CharField(max_length=20,choices=Status.choices,default=Status.NEW)
    message = models.TextField(blank=True)
    interested_product = models.CharField(max_length=200,blank=True)
    owner_note = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.get_status_display()}"