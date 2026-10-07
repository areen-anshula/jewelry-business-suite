from catalog.models import Product, Stock
from .exceptions import ProductNotFoundError, ProductNotActiveError, InvalidQuantityError, InsufficientStockError, StockUnavailableError
from .exceptions import InvalidOrderStatusError, OrderNotFoundError
from .models import Order, OrderItem
from django.db import transaction

class OrderService:

    @staticmethod
    def create_order(customer, shipping_address, product_id, quantity):
        with transaction.atomic():
            try:
                product = Product.objects.get(id=product_id)
            except Product.DoesNotExist:
                raise ProductNotFoundError("Product does not exist")

            if product.status != product.Status.ACTIVE:
                raise ProductNotActiveError("Product is not active")  

            if quantity <= 0:
                raise InvalidQuantityError("Quantity must be greater than zero")

            try:
                product_stock = Stock.objects.select_for_update().get(product=product)
            except Stock.DoesNotExist:
                raise StockUnavailableError("Stock is not available")

            if quantity > product_stock.stock_quantity :
                raise InsufficientStockError("Stock is not enough")

            order = Order.objects.create(
                customer = customer,
                shipping_address = shipping_address,
                status = Order.Status.PENDING,
            )

            order_item = OrderItem.objects.create(
                order = order,
                product = product,
                quantity = quantity,
                unit_price = product.price,
            )

            new_stock = product_stock.stock_quantity - quantity
            product_stock.stock_quantity = new_stock
            product_stock.save()

        return order   

    @staticmethod
    def confirm_order(order_id):
        with transaction.atomic():
            try:
                order = Order.objects.select_for_update().get(id=order_id)
            except Order.DoesNotExist:
                raise OrderNotFoundError("Order is not found")

            if order.status != Order.Status.PENDING:
                raise InvalidOrderStatusError("Only pending orders can be confirmed.")

            order.status = Order.Status.CONFIRMED
            order.save(update_fields=["status"])

        return order  

    @staticmethod
    def cancel_order(order_id):
        with transaction.atomic():
            try:
                order = Order.objects.select_for_update().get(id=order_id)
            except Order.DoesNotExist:
                raise OrderNotFoundError("Order is not found")

            if order.status not in [Order.Status.PENDING, Order.Status.CONFIRMED]:
                raise InvalidOrderStatusError("Only confirmed and pending orders can be canceled.") 

            order_items = OrderItem.objects.filter(order=order)  

            for order_item in order_items :
                try: 
                    stock = Stock.objects.select_for_update().get(product=order_item.product)
                except Stock.DoesNotExist:
                    raise StockUnavailableError("Stock is not available for this product.")

                stock.stock_quantity += order_item.quantity
                stock.save(update_fields=["stock_quantity"])

            order.status = Order.Status.CANCELLED
            order.save(update_fields=["status"])

        return order        
                    


