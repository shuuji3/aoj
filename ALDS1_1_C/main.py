import math


def is_prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


n = int(input())
count = 0
for _ in range(n):
    m = int(input())
    if is_prime(m):
        count += 1
print(count)
