# Advent of Code Day 1

file_path = 'input'


def find_first_digit(line):
    for char in line:
        if char.isdigit():
            return char
    return 0


def process_line(line):
    print(line)


try:
    with open(file_path, 'r') as file:
        for line in file:
            digit = find_first_digit(line.strip())
            print(digit)
except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
