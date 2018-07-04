import sys

for line in sys.stdin:
    number = int(line)
    prime = True
    # print(int(pow(number, 0.5)))
    for factor in range(2, int(pow(number, 0.5)) + 1):
        if number % factor == 0:
            prime = False
            break
        else:
            continue
    if prime == True:
        print("質數")
    else:
        print("非質數")