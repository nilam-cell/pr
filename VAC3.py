# Write a Python program to compute sine values from 0° to 90° using Aryabhata’s
# recursive method.
import math

step = 1                      
h = math.radians(step)        # convert step to radians

sinx = 0                      # sin(0°)
cosx = 1                      # cos(0°)

print("Angle   Sine Value")
print("-------------------")

for angle in range(0, 91, step):
    print(angle, "   ", round(sinx, 6))
    
    # Recursive formula
    sin_new = sinx + h * cosx
    cos_new = cosx - h * sinx
    
    sinx = sin_new
    cosx = cos_new
