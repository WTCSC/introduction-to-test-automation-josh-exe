import pytest
import math_it_up

"""
This file contains the tests for the math_it_up module, which contains the
following functions:

- math_it_up.is_even
- math_it_up.is_odd
- math_it_up.mean
- math_it_up.median
- math_it_up.mode

The `is_even` and `is_odd` functions accept a single argument, a number, and
return True if the number is even or odd, respectively.

The `mean` function accepts a single argument, a list of numbers, and returns
the mean of the numbers.

The `median` function accepts a single argument, a list of numbers, and returns
the median of the numbers.

The `mode` function accepts a single argument, a list of numbers, and returns
the mode of the numbers.

To run the tests, run `pytest` from the command line in the same directory as
this file.
"""

def test_is_even():
  assert math_it_up.is_even(2) == True
  assert math_it_up.is_even(16) == True
  assert math_it_up.is_even(17) == False
  assert math_it_up.is_even(-12) == True
  assert math_it_up.is_even(-1) == False
 
def test_is_odd():
  assert math_it_up.is_odd(3) == True
  assert math_it_up.is_odd(14) == False
  assert math_it_up.is_odd(23) == True
  assert math_it_up.is_odd(91) == True
  assert math_it_up.is_odd(123123123) == True

def test_mean():
  assert math_it_up.mean([1, 2, 3, 4, 5]) == 3
  assert math_it_up.mean([2, 6, 7, 30]) == 11.25
  assert math_it_up.mean([3, 6, 1, 2, 5, 10]) == 4.5
  assert math_it_up.mean([7, 3, 7, 8, 2, 22]) == 8.166666666666666
  assert math_it_up.mean([9, 8, 7, 6, 5, 4, 3, 2, 1]) == 5

def test_median():
  assert math_it_up.median([1, 2, 2, 6, 6, 7, 9]) == 6
  assert math_it_up.median([4, 4, 8, 9, 10]) == 8
  assert math_it_up.median([1, 5, 6, 8, 8, 9, 11, 24]) == 8
  assert math_it_up.median([1, 1, 3, 4, 5, 6, 7, 7]) == 4.5
  assert math_it_up.median([8, 8, 12, 13, 17, 20, 21, 30]) == 15

def test_mode():
  assert math_it_up.mode([1, 12, 13, 21, 21]) == [21]
  assert math_it_up.mode([2, 2, 5, 6, 8, 9, 10]) == [2]
  assert math_it_up.mode([3, 4, 5, 6, 7, 8]) == [3, 4, 5, 6, 7, 8]
  assert math_it_up.mode([5, 6, 12, 12, 12, 89, 235, 1000]) == [12]
  assert math_it_up.mode([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3]) == [1, 2]