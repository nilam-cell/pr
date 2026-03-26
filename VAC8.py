# Write a Python code Using Vyastisamanstih, expand: (x + 5)(x + 7)

a = int(input("Enter a: "))  # Coefficient of x in (x + 5)
b = int(input("Enter b: "))  # Constant in first binomial
c = int(input("Enter c: "))  # Coefficient of x in (x + 7)
d = int(input("Enter d: "))  # Constant in second binomial

# Step 1: Multiply x terms
x2_term = a * c

# Step 2: Cross addition for x term
x_term = a * d + b * c

# Step 3: Multiply constants
constant_term = b * d

# Display the expanded form
print(f"Expanded form: {x2_term}x^2 + {x_term}x + {constant_term}")
