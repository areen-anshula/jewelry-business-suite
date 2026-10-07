from django.urls import path
from .views import create_order, confirm_order, cancel_order
from . import views

urlpatterns = [
    path("create/", create_order, name="create_order"),
    path("<uuid:order_id>/confirm/",views.confirm_order,name="confirm_order",),
    path("<uuid:order_id>/cancel/",views.cancel_order,name="cancel_order",),
]