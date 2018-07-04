import sys

for t in sys.stdin:
    for i in range(int(t)):
        num = sys.stdin.readline()
        if len(num.split()) > 3:
            a, b, c, d = num.split()

            if int(a) * int(d) == int(b) * int(c):
                print(a, b, c, d, end=' ')
                print(int(int(d) * (int(b) / int(a))))
            else:
                print(a, b, c, d, end=' ')
                print(int(d) + int(b) - int(a))
