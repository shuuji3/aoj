n = int(input())
max_diff = -10**10

current_min = int(input())

for _ in range(n-1):
    current = int(input())
    diff = current - current_min
    if diff > max_diff:
        max_diff = diff
    if current < current_min:
        current_min = current
print(max_diff)
