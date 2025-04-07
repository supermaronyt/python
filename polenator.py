array = [[1 for _ in range(9)] for _ in range(5)]

for row in array:
    row[4] = 3

array[2] = [7] * 9

for row in array:
    print(row)
