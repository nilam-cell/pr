''' Write a Python program to verify the trigonometric identity
sin²θ + cos²θ = 1
for an angle entered by the user (in degrees).'''
import math
angle = float(input("Enter angle in degrees: "))
radian = math.radians(angle)

result = math.sin(radian)**2 + math.cos(radian)**2

print("Value of sin²θ + cos²θ =", result)

if round(result, 5) == 1:
    print("Identity Verified!")
else:
    print("Identity Not Verified!")
