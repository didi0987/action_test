import unittest
import time
import math

print("hello, action!!")


def add(a, b):
    return a + b


def my_sum(*nums):
    sum = 0
    for num in nums:
        sum += num
    return sum + 1


def abs(n):
    """
    Function to get absolute value of number.

    Example:

    >>> abs(1)
    1
    >>> abs(-1)
    1
    >>> abs(0)
    0
    """
    return n if n >= 0 else (-n)


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b


# HW2.Q2
def moveZeroes(nums):
    left = 0
    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
    return nums


# HW2.Q3
def area_square(x):
    return x * x


def area_rectangle(width, length):
    return width * length


def area_circle(x):
    x = x / 2
    return 3.14 * (x) ** 2


def area_difference(x, calc_area1, calc_area2):
    return abs(calc_area1(x) - calc_area2(x))


def area_ratio(x, calc_area1, calc_area2):
    return calc_area1(x) / calc_area2(x)


def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


class Mylist(list):
    pass
