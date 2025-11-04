# number of works
N = int(input())

for i in range(N):
    SH, SM, EH, EM = map(int, input().split())

    # convert both times to minutes
    start = SH * 60 + SM
    end = EH * 60 + EM

    # difference in minutes
    diff = end - start

    # convert back to hours and minutes
    hours = diff // 60
    minutes = diff % 60

    print(hours, minutes)
