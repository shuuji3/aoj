s = input()
q = int(input())
for i in range(q):
    line = input()
    if 'print' in line:
        op, a, b = line.split()
        a = int(a)
        b = int(b)
        print(s[a:b+1])
    elif 'reverse' in line:
        op, a, b = line.split()
        a = int(a)
        b = int(b)
        reversed_substring = ''.join(list(reversed(s[a:b+1])))
        s = s[:a] + reversed_substring + s[b+1:]
    elif 'replace' in line:
        op, a, b, p = line.split()
        a = int(a)
        b = int(b)
        s = s[:a] + p + s[b+1:]
