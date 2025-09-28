import pytest
from ..boat_movements import can_travel_to

game_matrix = [
    [False, True,  True,  False, False, False],
    [True,  True,  True,  False, False, False],
    [True,  True,  True,  True,  True,  True],
    [False, True,  True,  False, True,  True],
    [False, True,  True,  True,  False, True],
    [False, False, False, False, False, False],
]

def test_should_return_true_for_valid_move():
  can_travel_to(game_matrix, 3, 2, 2, 2) # True, Valid move
  ...
  
def test_should_return_false_for_movement_through_land():
  can_travel_to(game_matrix, 3, 2, 3, 4) # False, Can't travel through land
  ...

def test_should_return_false_for_out_of_bounds():
  can_travel_to(game_matrix, 3, 2, 6, 2) # False, Out of bounds
  ...



