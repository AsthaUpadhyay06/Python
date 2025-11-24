# Input number of people
N = int(input())

# Minimum skill required
X = int(input())

# Check each person's skill
for i in range(N):
    Y = int(input())
    if Y >= X:
        print("YES")
    else:
        print("NO")
