import sys

for row_column in sys.stdin:
    row, column = row_column.split()
    row = int(row)
    column = int(column)
    element = [[None]*column for i in range(row)]
    answer = [[None]*row for i in range(column)]
    # print(element)
    for row_number in range(0, row):
        element[row_number] = sys.stdin.readline().split()
    # print(element)
    for j in range(0, row):
        for k in range(0, column):
            answer[k][j] = element[j][k]
            # print(element[j][k])
    for l in range(0, column):
        for m in range(0, row):
            print(answer[l][m], end=" ")
        print("")
    print("")