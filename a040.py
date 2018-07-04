import sys

for line in sys.stdin:
    n, m = line.split()
    N = int(n)
    M = int(m)
    armstrong = False
    for number in range(N, M):
        number_digit = number
        digit = 1
        number_calculate = number
        calculate = 0
        # print(number)
        while int(number_digit / 10) != 0:
            digit = digit + 1
            number_digit = int(number_digit / 10)
            # print(number_digit)
        for arnstrong_add in range(0, digit):
            calculate = int(calculate + pow((number_calculate % 10), digit))
            number_calculate = int(number_calculate / 10)
        # print(number, end=" ")
        # print(calculate)
        if calculate == number:
            armstrong = True
            print(number, end=" ")
            # print(number)
        else:
            print("", end="")

    if armstrong == False:
        print("none")
    else:
        print("")
