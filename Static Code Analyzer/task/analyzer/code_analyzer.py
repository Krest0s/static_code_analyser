path = input()
file = open(path, 'r')
for number, line in enumerate(file):
    if len(line) > 79:
        print(f'Line {number + 1}: S001 Too long')
file.close()
