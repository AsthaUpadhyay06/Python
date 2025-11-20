import math

A, B = map(int, input().split())

result = A / B
floor_val=math.floor(result)
ceil_val=math.ceil(result)
round=math.floor(result+0.5)
print(f"floor {A} / {B} = {floor_val}")
print(f"ceil {A} / {B} = {ceil_val}")
print(f"round {A} / {B} = {round}")
