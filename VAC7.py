# Write a Python code Using Yavadunam, compute: 97 × 104
base = int(input("Enter base: "))
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

# Deviations from base
d1 = num1 - base
d2 = num2 - base

# Step 1: Cross addition
left_part = num1 + d2  # or num2 + d1

# Step 2: Multiply deviations
right_part = d1 * d2

# Adjust if right part is negative
if right_part < 0:
    left_part -= 1
    right_part = base + right_part

# Final result
result = left_part * base + right_part

print("Result using Yavadunam:", result)
