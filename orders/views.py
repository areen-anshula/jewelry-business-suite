from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required
from customers.models import Address
from .services import OrderService
from django.views.decorators.http import require_POST
from .exceptions import OrderNotFoundError, InvalidOrderStatusError


@login_required
def create_order(request):
    if request.method == "POST":
        customer = request.user.customer_profile
        product_id = request.POST.get("product_id")
        try:
            quantity = int(request.POST.get("quantity"))
        except ValueError:
            raise ValueError("Quantity must be a valid number")    
        shipping_address_id = request.POST.get("shipping_address_id")
        
        shipping_address = Address.objects.get(id = shipping_address_id, customer = customer)

        order = OrderService.create_order(
            customer=customer,
            shipping_address=shipping_address,
            product_id=product_id,
            quantity=quantity,
        )
    
    return HttpResponse(f"Created order: {order.id}")

#@login_required
@require_POST
def confirm_order(request, order_id):
    try:
        order = OrderService.confirm_order(order_id)

        return JsonResponse({
            "success" : True,
            "message" : "Order confirmed successfully.",
            "order_id": str(order.id),
            "status" : order.status,
        })
    
    except OrderNotFoundError as e:
        return JsonResponse({
            "success": False,
            "error": str(e),
        }, status=404)

    except InvalidOrderStatusError as e:
        return JsonResponse({
            "success": False,
            "error": str(e),
        }, status=400)


def cancel_order(request, order_id):
    try:
        order = OrderService.cancel_order(order_id)

        return JsonResponse({
            "success": True,
            "message": "Order cancelled successfully.",
            "order_id": str(order.id),
            "status": order.status,
        })

    except OrderNotFoundError as e:
        return JsonResponse({
            "success": False,
            "error": str(e),
        }, status=404)

    except InvalidOrderStatusError as e:
        return JsonResponse({
            "success": False,
            "error": str(e),
        }, status=400)    
