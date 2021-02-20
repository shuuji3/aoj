# TDOO: fix TLE

clock = 0
tasks: (str, int) = []

# input
n, q = map(int, input().split())
for i in range(n):
    name, time_str = input().split()
    time = int(time_str)
    tasks.append((name, time))

# scheduling
while len(tasks) > 0:
    task = tasks[0]
    tasks = tasks[1:]

    name, remaining_time = task
    clock += min(remaining_time, q)
    if remaining_time <= q:
        print(name, clock)
    else:
        task = (name, remaining_time - q)
        tasks.append(task)
