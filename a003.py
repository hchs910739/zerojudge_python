import sys

for line in sys.stdin:
    M, D = line.split()
    S = (int(M) * 2 + int(D)) % 3

    if S == 0:
        print("普通")
    elif S == 1:
        print("吉")
    else:
        print("大吉")

