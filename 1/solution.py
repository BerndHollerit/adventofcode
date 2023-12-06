# Advent of Code Day 1

file_path = 'input'


def process_line(line):
    print(line)


try:
    with open(file_path, 'r') as file:
        for line in file:
            process_line(line.strip())
except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
