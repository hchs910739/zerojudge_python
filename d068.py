import sys

for weight in sys.stdin:
    if int(weight) > 50 :
        print(int(weight) - 1)
    else:
        print(int(weight))