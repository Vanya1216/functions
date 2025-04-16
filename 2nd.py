import math

# Asking the user for a number as input
num = float(input("Enter a number: "))

# Calculating the required values
square_root = math.sqrt(num)
natural_log = math.log(num)
sine_value = math.sin(num)

# Displaying the results
print(f"Square root of {num}: {square_root}")
print(f"Natural logarithm (log base e) of {num}: {natural_log}")
print(f"Sine of {num} (in radians): {sine_value}")