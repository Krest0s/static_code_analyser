def print_info(number_index, warn_index, message):
    print(f'Line {number_index}: S00{warn_index} {message}')


def too_long(line_file, number_index):
    if len(line_file) > 79:
        print_info(number_index, 1, 'Too long')


def indentation(line_file, number_index):
    low_letters = str([chr(x) for x in range(97, 123)])  # create lower letters abc
    up_letters = low_letters.upper()
    spaces = 0
    for symbol in line_file:
        if symbol == " " and symbol not in low_letters and symbol not in up_letters:
            spaces += 1
        else:
            break


path = 'bad_code.py'
file = open(path, 'r')
for number, line in enumerate(file):
    too_long(line, number)
    indentation(line, number)
file.close()
