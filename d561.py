import sys

for number in sys.stdin:
    N = float(number)
    answer = round(N, 2)
    print("%.2f" % answer)
