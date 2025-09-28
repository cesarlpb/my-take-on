from enum import Enum, auto
from typing import Callable

class DiscountType(Enum):
    STANDARD = auto()
    SEASONAL = auto()
    WEIGHT = auto()

# cannot edit ^

STANDARD_DISCOUNT = 6 * 1.0
SEASONAL_DISCOUNT = 12 * 1.0
WEIGHT_DISCOUNT = 18 * 1.0

discount_map: dict[DiscountType, Callable[[float], float]] = {
  DiscountType.STANDARD: lambda _: STANDARD_DISCOUNT,
  DiscountType.SEASONAL: lambda _: SEASONAL_DISCOUNT,
  DiscountType.WEIGHT: lambda cart_weight: STANDARD_DISCOUNT if cart_weight <= 10 else WEIGHT_DISCOUNT
}

def apply_discount(total_price: float, discount: float) -> float:
  return round(total_price * (1 - discount / 100), 2)

def validate_inputs(cart_weight: float, total_price: float, discount_type: DiscountType) -> None:
    if cart_weight <= 0:
        raise ValueError("weight must be positive")

    if total_price < 0:
        raise ValueError("price cannot be negative")

    if not isinstance(discount_type, DiscountType):
        raise TypeError("discount_type must be an instance of DiscountType")

def get_discounted_price(cart_weight: float, total_price: float, discount_type: DiscountType) -> float:
    validate_inputs(cart_weight, total_price, discount_type)
    fn = discount_map.get(discount_type, lambda _: STANDARD_DISCOUNT)
    return apply_discount(total_price, fn(cart_weight))