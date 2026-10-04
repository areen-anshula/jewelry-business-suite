from django.urls import path
from .views import create_order, confirm_order, cancel_order

urlpatterns = [
    path("create/", create_order, name="create_order"),
    path("orders/<uuid:order_id>/confirm/",confirm_order,name="confirm_order",),
    path("orders/<uuid:order_id>/cancel/",cancel_order,name="cancel_order",),
]