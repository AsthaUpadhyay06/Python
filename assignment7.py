# Number of test cases
N = int(input())

for _ in range(N):
    a, b = map(int, input().split())
    a = a % 10  # only last digit matters

    # patterns of last digits
    
    