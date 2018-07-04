import sys

for line in sys.stdin:
    if len(line.split()) > 2:
        a, z, b = line.split()
        # print(a)
        # print(z)
        # print(b)
        if z == '+':
            print(int(a) + int(b))
        elif z == '-':
            print(int(a) - int(b))
        elif z == '*':
            print(int(a) * int(b))
        elif z == '/':
            print(int(a) // int(b))
        else:
            print("")