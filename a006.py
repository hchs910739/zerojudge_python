import sys

for equation in sys.stdin:
    if len(equation.split()) > 2:
        a, b, c = equation.split()
        A = int(a)
        B = int(b)
        C = int(c)
        root_1 = ((B * (-1)) + pow(B * B - 4 * A * C, 0.5)) / (2 * A)
        root_2 = ((B * (-1)) - pow(B * B - 4 * A * C, 0.5)) / (2 * A)
        if B * B - 4 * A * C > 0:
            print("Two different roots x1=", end="")
            print(int(root_1), end=" , x2=")
            print(int(root_2))
        elif B * B - 4 * A * C == 0:
            print("Two same roots x=", end="")
            print(int(root_1))
        else:
            print("No real root")