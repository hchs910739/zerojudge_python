import sys

for how_long in sys.stdin:
    long = int(how_long)
    # print(long)
    number = sys.stdin.readline().split()
    for j in range(0, long):
        number[j] = int(number[j])
    # print(number)
    # print(sorted(number))
    answer = sorted(number)
    for i in range(0, long):
        print(answer[i], end=" ")
    print("")