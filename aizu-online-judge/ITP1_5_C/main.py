while True:
    h, w = map(int, input().split())

    if h == 0 and w == 0:
        break

    c1 = '#'
    c2 = '.'
    for i in range(h):
        for j in range(w):
            if j % 2 == 0:
                print(c1, end='')
            else:
                print(c2, end='')
        print()
        c1, c2 = c2, c1
    print()
