from pathlib import Path

INPUT_PATH = Path(__file__).parent.parent.joinpath("inputs/day2.txt")
LINE_LENGTH = None

def get_inputs():
    with INPUT_PATH.open("r") as text_file:
        input_lines =  [number.split(" ") for number in [line.strip() for line in text_file.readlines()]]
    return input_lines

def remove_digit(line, index):
    print(line)
    new_line = []
    for index_, digit in enumerate(line):
        if not index_ == index:
            new_line.append(digit)
    print(new_line)
    return new_line

def is_safe(line):
    global LINE_LENGTH
    length = len(line)

    if not length == LINE_LENGTH - 1 and not length == LINE_LENGTH:
        return False

    direction = 0
    for i in range(len(line)):
        change = 0

        first_number = int(line[i])
        try:
            second_number = int(line[i + 1])
        except IndexError:
            change += first_number
            break

        change += first_number - second_number

        if not -3 <= change <= 3 or change == 0:
            new_line = remove_digit(line, i)
            is_safe(new_line)

        if change > 0:
            direction += 1
            continue

        direction -= 1

    return abs(direction) == len(line) - 1

if __name__ == '__main__':
    lines = get_inputs()

    result = 0
    for line_ in lines:
        LINE_LENGTH = len(line_)
        if is_safe(line_):
            result += 1
    print(result)
