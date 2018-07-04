import sys

for line in sys.stdin:
    a, n = line.split()
    a = int(a)
    n = int(n)
    n = n % 10007
    print(pow(a, n) % 10007)