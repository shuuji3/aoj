taro_point = 0
hanako_point = 0

n = int(input())
for i in range(n):
    taro, hanako = input().split()
    if taro == hanako:
        taro_point += 1
        hanako_point += 1
    elif taro > hanako:
        taro_point += 3
    else:
        hanako_point += 3
print(taro_point, hanako_point)
