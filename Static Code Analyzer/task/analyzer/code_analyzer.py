import re
import sys
import os
import pathlib


def print_info(file_name, number_index, warn_index, message):
    print(f'{file_name}: Line {number_index + 1}: S00{warn_index} {message}')


def too_long(line_file, number_index, file_name):
    if len(line_file) > 79:
        print_info(file_name, number_index, 1, 'Too long')


def indentation(line_file, number_index, file_name):
    if line_file[0] == ' ':
        if len(re.match(' +', line_file).group(0)) % 4 != 0:
            print_info(file_name, number_index, 2, 'Indentation is not a multiple of four')


def semicolon(line_file, number_index, file_name):
    lattice = line_file.find('#') == 0  # line starts with #
    # conditions to avoid
    string = re.search("\'.*\'", line_file)
    semicolon_string = string is not None and ';' in string.group(0)  # check if exists 'string' and ; in it
    lattice_semicolon = re.search('#.*;', line_file)  # check if ; after #
    if lattice or semicolon_string or lattice_semicolon:
        return
    if re.match(".*;", line_file):
        print_info(file_name, number_index, 3, 'Unnecessary semicolon')


def two_spaces(line_file, number_index, file_name):
    if re.search("[^ ]{2}#", line_file) or re.search("[^ ] #", line_file):
        if re.search('#.*#', line_file):
            return
        print_info(file_name, number_index, 4, 'At least two spaces required before inline comments')


def todo(line_file, number_index, file_name):
    if re.search('#.*todo.*', line_file, re.IGNORECASE):
        print_info(file_name, number_index, 5, 'TODO found')


def blank_lines(line_file, number_index, file_name):
    first_symbols.append(line_file[0])
    count = 0
    if first_symbols[-1] != '\n':
        for i in reversed(first_symbols[:-1]):
            if i == '\n':
                count += 1
            else:
                break
        if count > 2:
            print_info(file_name, number_index, 6, 'More than two blank lines used before this line')


def analyze_file(file_name):
    file = open(file_name, 'r')
    for number, line in enumerate(file):
        too_long(line, number, file_name)
        indentation(line, number, file_name)
        semicolon(line, number, file_name)
        two_spaces(line, number, file_name)
        todo(line, number, file_name)
        blank_lines(line, number, file_name)
    file.close()


first_symbols = []
if os.path.isdir(sys.argv[1]):
    for address, dirs, files in os.walk(sys.argv[1]):
        for name in files:
            if pathlib.Path(name).suffix == '.py':  # if script in folder
                analyze_file(os.path.join(address, name))
else:
    analyze_file(sys.argv[1])
