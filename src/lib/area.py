"""
area.py
=======

This module provides functions to calculate the area of different shapes.
"""
from lib.calculator import Calculator

PI = 3.14159


def square(side):
    """
    Returns the area of a square.

    Args:
        side (float): The side of the square.

    Returns:
        float: The area of the square.
    """
    return Calculator(side).square()


def rectangle(length, width):
    """
    Returns the area of a rectangle.

    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The area of the rectangle.
    """
    return Calculator(length).multiply(width)


def circle(radius):
    """
    Returns the area of a circle.

    Args:
        radius (float): The radius of the circle.

    Returns:
        float: The area of the circle.
    """
    global PI
    calc = Calculator(radius)
    calc.square()
    return calc.multiply(PI)
