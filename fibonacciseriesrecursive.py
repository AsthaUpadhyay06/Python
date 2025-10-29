# n = int(input("Enter number of terms: "))
# a, b = 0, 1
# for _ in range(n):
#     print(a, end=" ")
#     a, b = b, a + b


# sum of n natural numbers
# n=5
# sum=0
# for i in range(1,n+1):
#     sum=sum+i

# print(sum)    


# recursive
def naturalsum(n):
    if n == 1:
        return 1
    else:
        return n + naturalsum(n - 1)
n = 5
result = natural_sum(n)
print("Sum of first", n, "natural numbers is:", result)