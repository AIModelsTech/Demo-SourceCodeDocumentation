"""
calculator.py
=============

This module provides a simple calculator class to perform basic arithmetic operations.
"""


class Calculator:
    """
    A simple calculator class to demonstrate Sphinx documentation.

    Attributes:
        value (float): The current value stored in the calculator.
    """

    def __init__(self, initial_value=0):
        """
        Initializes the calculator with an optional initial value.

        Args:
            initial_value (float, optional): The starting value of the calculator. Defaults to 0.
        """
        self.value = initial_value

    def add(self, amount):
        """
        Adds a number to the current value.

        Args:
            amount (float): The number to be added to the current value.

        Returns:
            float: The updated value after addition.
        """
        self.value += amount
        return self.value

    def subtract(self, amount):
        """
        Subtracts a number from the current value.

        Args:
            amount (float): The number to be subtracted from the current value.

        Returns:
            float: The updated value after subtraction.
        """
        self.value -= amount
        return self.value

    def multiply(self, factor):
        """
        Multiplies the current value by a given factor.

        Args:
            factor (float): The factor to multiply the current value by.

        Returns:
            float: The updated value after multiplication.
        """
        self.value *= factor
        return self.value

    def divide(self, divisor):
        """
        Divides the current value by a given divisor.

        Args:
            divisor (float): The divisor to divide the current value by.

        Returns:
            float: The updated value after division.

        Raises:
            ValueError: If division by zero is attempted.
        """
        if divisor == 0:
            raise ValueError("Cannot divide by zero.")
        self.value /= divisor
        return self.value

    def square(self):
        """
        Squares the current value.

        Returns:
            float: The square of the current value.
        """
        self.value = self.value**2
        return self.value
