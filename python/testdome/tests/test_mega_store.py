import pytest
from ..mega_store import DiscountType, get_discounted_price

def test_should_apply_discount_weight_correctly():
  assert get_discounted_price(12, 100, DiscountType.WEIGHT) == 82.0
  
def test_should_apply_discount_standard_correctly():
  assert get_discounted_price(12, 100, DiscountType.STANDARD) == 94.0
  
def test_should_apply_discount_seasonal_correctly():
  assert get_discounted_price(12, 100, DiscountType.SEASONAL) == 88.0
  
def test_incorrect_weight_should_raise_value_error():
  with pytest.raises(ValueError, match="weight cannot be negative or zero"):
    get_discounted_price(-12, 100, DiscountType.STANDARD)
    
def test_incorrect_price_should_raise_value_error():
  with pytest.raises(ValueError, match="price cannot be negative"):
    get_discounted_price(12, -100, DiscountType.STANDARD)
  
def test_incorrect_discount_type_should_raise_type_error():
  with pytest.raises(TypeError, match="discount_type should be DiscountType class"):
    get_discounted_price(12, 100, "Standard")