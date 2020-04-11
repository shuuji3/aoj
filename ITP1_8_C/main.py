from collections import Counter
import string

counter = Counter()
while True:
    try:
        s = input().lower()
        counter += Counter(s)
    except EOFError:
        break

for c in string.ascii_lowercase:
    count = counter[c]
    print(f'{c} : {count}')
