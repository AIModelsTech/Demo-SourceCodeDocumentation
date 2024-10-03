"""
run.py
======

This module provides a simple script to demonstrate the use of the area module.
"""
import sys

from lib import area


def main():
    """
    Main function to run the area calculator.

    Returns:
        int: The exit code.
    """
    print("Welcome to the Area Calculator!")
    try:
        while True:
            print("Available shapes: (S)quare, (R)ectangle, (C)ircle or (Q)uit")
            shape = input("Enter the shape (S/R/C): ").strip().lower()
            if shape == "s":
                side = float(input("Enter the side of the square: "))
                print(f"The area of the square is: {area.square(side)}")
            elif shape == "r":
                length = float(input("Enter the length of the rectangle: "))
                width = float(input("Enter the width of the rectangle: "))
                print(f"The area of the rectangle is: {area.rectangle(length, width)}")
            elif shape == "c":
                radius = float(input("Enter the radius of the circle: "))
                print(f"The area of the circle is: {area.circle(radius)}")
            elif shape == "q":
                print("Thank you for using the Area Calculator!")
                break
            else:
                print("Invalid choice. Please try again.")
    except ValueError as e:
        print(f"Error: {e}")
        return 1
    except KeyboardInterrupt:
        print("\nProcess interrupted. Exiting...")
        return 1
    return 0


if __name__ == "__main__":
    ret = main()
    sys.exit(ret)
