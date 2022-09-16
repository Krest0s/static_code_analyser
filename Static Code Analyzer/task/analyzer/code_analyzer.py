import re


def print_info(number_index, warn_index, message):
    print(f'Line {number_index + 1}: S00{warn_index} {message}')


def too_long(line_file, number_index):
    if len(line_file) > 79:
        print_info(number_index, 1, 'Too long')


def indentation(line_file, number_index):
    if line_file[0] == ' ':
        if len(re.match(' +', line_file).group(0)) % 4 != 0:
            print_info(number_index, 2, 'Indentation is not a multiple of four')


def semicolon(line_file, number_index):
    string = re.search("\'.*\'", line_file)
    if line_file.find('#') == 0 or string is not None and ';' in string.group(0):
        return
    if re.match(".*;", line_file):
        print_info(number_index, 3, 'Unnecessary semicolon')


def two_spaces(line_file, number_index):
    if re.search("[^ ] #", line_file):
        print_info(number_index, 4, 'At least two spaces required before inline comments')


def todo(line_file, number_index):
    if re.search('#.*todo.*', line_file, re.IGNORECASE):
        print_info(number_index, 5, 'TODO found')


def blank_lines(line_file, number_index):
    first_symbols.append(line_file[0])
    first_symbols2 = ' '.join(first_symbols)
    print('1', first_symbols2)

path = 'bad_code.py'
file = open(path, 'r')
first_symbols = []
for number, line in enumerate(file):
    # too_long(line, number)
    # indentation(line, number)
    # semicolon(line, number)
    # two_spaces(line, number)
    # todo(line, number)
    blank_lines(line, number)
file.close()
