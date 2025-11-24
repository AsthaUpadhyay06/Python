import math

# number of test cases
T = int(input())

for i in range(T):
    X, Y = map(int, input().split())

    gcd = math.gcd(X, Y)
    lcm = (X * Y) // gcd

    print(gcd, lcm)
