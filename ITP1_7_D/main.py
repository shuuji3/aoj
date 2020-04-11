n, m, l = map(int, input().split())

A = []
for i in range(n):
    row = list(map(int, input().split()))
    A.append(row)

B = []
for i in range(m):
    row = list(map(int, input().split()))
    B.append(row)

C = []
for i in range(n):
    row = []
    for j in range(l):
        sum = 0
        for k in range(m):
            sum += A[i][k] * B[k][j]
        row.append(sum)
    C.append(row)

for i in range(n):
    print(' '.join(map(str, C[i])))
