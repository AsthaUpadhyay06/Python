amount = int(input("Enter total amount: "))
denom = int(input("Enter starting denomination: "))
print()

match denom:
    case 100:
        print(f"100 rupees note: {amount // 100}")
        amount %= 100
        # continue to next case
        denom = 50

    case 50:
        print(f"50 rupees note: {amount // 50}")
        amount %= 50
        denom = 20

    case 20:
        print(f"20 rupees note: {amount // 20}")
        amount %= 20
        denom = 10

    case 10:
        print(f"10 rupees note: {amount // 10}")
        amount %= 10
        denom = 5

    case 5:
        print(f"5 rupees note: {amount // 5}")
        amount %= 5
        denom = 2

    case 2:
        print(f"2 rupees note: {amount // 2}")
        amount %= 2
        denom = 1

    case 1:
        print(f"1 rupees note: {amount // 1}")
