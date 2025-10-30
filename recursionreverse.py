
def reverse_print(n):
    if n<1:
        return
    print(n)
    reverse_print(n-1)

n = 5
# print(n)
reverse_print(n)



