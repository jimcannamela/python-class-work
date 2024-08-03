# Example 1: Basic Arithmetic Operations
# Performing basic arithmetic like square root and power calculations.

import math

# Square root
print("Square root of 16:", math.sqrt(16))

# Power
print("3 raised to the power of 4:", math.pow(3, 4))

# Example 2: Trigonometric Functions
# The math module provides functions to perform standard trigonometric calculations.

import math

# Sine, Cosine, and Tangent
angle = math.radians(45)  # Converting degrees to radians
print("Sine of 45 degrees:", math.sin(angle))
print("Cosine of 45 degrees:", math.cos(angle))
print("Tangent of 45 degrees:", math.tan(angle))

# Example 3: Exponential and Logarithmic Functions
# Calculating exponents and logarithms.

import math

# Exponential
print("e^2:", math.exp(2))

# Logarithm
print("Natural logarithm of 10:", math.log(10))
print("Base-10 logarithm of 10:", math.log10(10))

# Example 4: Rounding Functions
# The math module provides functions for rounding numbers.

import math

num = 14.5678

# Floor
print("Floor of 14.5678:", math.floor(num))

# Ceiling
print("Ceiling of 14.5678:", math.ceil(num))

# Example 5: Mathematical Constants
# Accessing mathematical constants.

import math

# Pi
print("Value of Pi:", math.pi)

# Euler's number
print("Value of Euler's number:", math.e)

# Example 6: Handling Complex Numbers
# While the math module doesn't directly handle complex numbers (use the cmath module for that), it provides support for related operations like fabs for absolute values.

import math

# Absolute value
print("Absolute value of -98.6:", math.fabs(-98.6))