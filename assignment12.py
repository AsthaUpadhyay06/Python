N = int(input())

i = 1  # round number

while N > 0:
    # Ramesh's turn
    if N - i <= 0:
        print("Ramesh")
        break
    N -= i

    # Suresh's turn
    if N - (2 * i) <= 0:
        print("Suresh")
        break
    N -= 2 * i

    i += 1
