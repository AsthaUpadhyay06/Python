def largest(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c

print("Largest number is:", largest(10, 25, 15))
