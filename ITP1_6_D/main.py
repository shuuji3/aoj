n, m = map(int, input().split())

A = []
for i in range(n):
    A.append(list(map(int, input().split())))
b = []
for i in range(m):
    b.append(int(input()))

for i in range(n):
    sum = 0
    for j in range(m):
        sum += A[i][j] * b[j]
    print(sum)
