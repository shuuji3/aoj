r, c = map(int, input().split())
table = []
for i in range(r):
    row = list(map(int, input().split()))
    row.append(sum(row))
    table.append(row)

total_row = []
for col in range(c+1):
    column_sum = 0
    for row in range(r):
        column_sum += table[row][col]
    total_row.append(column_sum)
table.append(total_row)

for i in range(r+1):
    print(' '.join(map(str, table[i])))
