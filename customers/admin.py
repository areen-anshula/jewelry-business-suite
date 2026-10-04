from django.contrib import admin
from customers.models import Country, Customer, Address

admin.site.register(Country)
admin.site.register(Customer)
admin.site.register(Address)
