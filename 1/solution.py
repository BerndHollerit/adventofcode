# Advent of Code Day 1

file_path = 'input'


def find_first_digit(line):
    for char in line:
        if char.isdigit():
            return char
    return 0


def find_last_digit(line):
    for char in reversed(line):
        if char.isdigit():
            return char
    return "No digit found"


def concatenate_digits(first_digit, last_digit):
    concatenated_result = str(first_digit) + str(last_digit)
    return int(concatenated_result)  # Convert the result back to an integer


def process_line(line):
    print(line)


try:
    with open(file_path, 'r') as file:
        for line in file:
            first_digit = find_first_digit(line.strip())
            last_digit = find_last_digit(line.strip())
            combination = concatenate_digits(first_digit, last_digit)

            print(combination)
except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
