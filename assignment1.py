import math

angle = 60       
r = 42       


length = (angle / 360) * 2 * math.pi * r

side = length / 4

area = side ** 2

print(f"Arc Length = {length:.2f} cm")
print(f"Side of Square = {side:.2f} cm")
print(f"Area of Square = {area:.2f} cm²")
print()
