import math

while True:
    n = int(input())
    if n == 0:
        break
    points = list(map(int, input().split()))

    m = sum(points) / n
    variance = sum(map(lambda x: (x - m) ** 2, points)) / n
    standard_deviation = math.sqrt(variance)
    print(standard_deviation)
