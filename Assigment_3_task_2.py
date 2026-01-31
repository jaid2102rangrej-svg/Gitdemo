import math

# 1. Ask user for input
num = float(input("Enter a number: "))

# 2. Perform calculations using math module
square_root = math.sqrt(num)
natural_log = math.log(num)       # log base e
sine_value = math.sin(num)        # input is in radians

# 3. Display results
print(f"Square root of {num} is: {square_root}")
print(f"Natural logarithm (ln) of {num} is: {natural_log}")
print(f"Sine of {num} (in radians) is: {sine_value}")
