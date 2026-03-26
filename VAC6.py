'''Write a Python program to calculate the area of a cyclic quadrilateral using  
Brahmagupta’s formula. The program should accept four sides as input and display  
the area. '''
import math

# Taking input from the user
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
d = float(input("Enter side d: "))

# Calculating the semiperimeter
s = (a + b + c + d) / 2

# Calculating the area using Brahmagupta’s formula
area = math.sqrt((s - a) * (s - b) * (s - c) * (s - d))

# Displaying the result
print("The area of the cyclic quadrilateral is:", area)
