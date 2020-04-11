s = int(input())

second = s % 60
s = s // 60
min = s % 60
hour = s // 60

print(f'{hour}:{min}:{second}')
