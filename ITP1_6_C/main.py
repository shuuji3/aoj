building_num = 4
floor_num = 3

m = []
for i in range(building_num):
    building = []
    for j in range(floor_num):
        floor = [0] * 10
        building.append(floor)
    m.append(building)

n = int(input())
for i in range(n):
    b, f, r, v = map(int, input().split())
    m[b-1][f-1][r-1] += v

delimiter = '#' * 20
for i in range(building_num):
    building = m[i]
    for floor in building:
        for room in floor:
            print(f' {room}', end='')
        print()

    if i != building_num - 1:
        print(delimiter)
