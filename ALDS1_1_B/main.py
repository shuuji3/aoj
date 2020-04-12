x, y = map(int, input().split())
if x < y:
    x, y = y, x

while True:
    x, y = y, x % y
    if y == 0:
        break
print(x)
