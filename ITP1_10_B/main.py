import math

a, b, C = map(float, input().split())
C = C / 180 * math.pi  # convert to radian

h = b * math.sin(C)
S = a * h / 2
c = math.sqrt((a - b * math.cos(C)) ** 2 + h ** 2)
L = a + b + c

print(S)
print(L)
print(h)
