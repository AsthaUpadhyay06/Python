def reverse_number(num):
    rev = 0
    while num > 0:
        rev = rev * 10 + (num % 10)
        num = num // 10
    return rev

n = int(input("Enter number of cases: "))

for i in range(n):
    a, b = map(int, input("Enter two numbers: ").split())


    a = reverse_number(a)
    b = reverse_number(b)


    s = a + b

    
    result = reverse_number(s)

    print(result)
