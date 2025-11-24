numbers = [10, 21, 4, 45, 66, 93]
odds = []
evens = []
for num in numbers:
    if num % 2 == 0:
        evens.append(num)
    else:
        odds.append(num)
print("Even numbers:", evens)
print("Odd numbers:", odds)