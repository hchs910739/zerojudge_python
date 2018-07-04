import sys

for day in sys.stdin:
    D = int(day)
    answer = 0
    number = sys.stdin.readline().split()
    # print(number)
    for i in range(0, D):
        number[i] = int(number[i])
        answer = answer + number[i] * (i+1)
    print(answer)