import math

n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

print(sum(map(lambda v: math.fabs(v[0] - v[1]), zip(x, y))))
print(sum(map(lambda v: math.fabs((v[0] - v[1]) ** 2), zip(x, y))) ** (1/2))
print(sum(map(lambda v: math.fabs((v[0] - v[1]) ** 3), zip(x, y))) ** (1/3))
print(max(map(lambda v: math.fabs(v[0] - v[1]), zip(x, y))))
