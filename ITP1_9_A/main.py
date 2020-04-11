word = input()

count = 0
while True:
    line = input()
    if line == 'END_OF_TEXT':
        break
    count += len(list(filter(lambda s: s.lower() == word, line.split())))

print(count)
