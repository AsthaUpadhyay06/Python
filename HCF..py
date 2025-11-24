# hcf of two number
def print_hcf(n1,n2):
    """Prints the highest common factor of two numbers."""
    if n1 > n2:
        smaller = n2
    else:
        smaller = n1
    for i in range(1, smaller + 1):
        if (n1 % i == 0) and (n2 % i == 0):
            hcf = i
    return hcf
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
hcf = print_hcf(n1,n2)
print("The HCF of", n1, "and", n2, "is",hcf)
