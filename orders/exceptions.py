class OrderError(Exception):
    pass

class ProductNotFoundError(OrderError):
    pass

class ProductNotActiveError(OrderError):
    pass

class InvalidQuantityError(OrderError):
    pass

class StockUnavailableError(OrderError):
    pass

class InsufficientStockError(OrderError):
    pass

class OrderNotFoundError(OrderError):
    pass

class InvalidOrderStatusError(OrderError):
    pass