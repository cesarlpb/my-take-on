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

def validate_inputs(cart_weight: float, total_price: float, discount_type: DiscountType) -> bool:
  is_cart_weight_valid = isinstance(cart_weight, (float, int)) and cart_weight > 0
  if not is_cart_weight_valid:
    raise ValueError("weight cannot be negative or zero")
  is_total_price_valid = isinstance(total_price, (float, int)) and total_price >= 0 # 0 -> product is free
  if not is_total_price_valid:
    raise ValueError("price cannot be negative")
  is_discount_type_valid = isinstance(discount_type, DiscountType)
  if not is_discount_type_valid:
    raise TypeError("discount_type should be DiscountType class")
  return is_cart_weight_valid and is_total_price_valid and is_discount_type_valid

def get_discounted_price(cart_weight: float, total_price: float, discount_type: DiscountType) -> float:
    inputs_are_valid = validate_inputs(cart_weight, total_price, discount_type)
    if inputs_are_valid:
      fn = discount_map.get(discount_type, lambda _: STANDARD_DISCOUNT)
      # print("Applied discount:", fn(cart_weight), "%") # Debug
      return apply_discount(total_price, fn(cart_weight))
    else:
      return float("nan")