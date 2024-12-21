from pathlib import Path

INPUT_PATH = Path(__file__).parent.parent.joinpath("inputs/day2.txt")

def get_inputs():
    with INPUT_PATH.open("r") as text_file:
        input_lines =  [number.split(" ") for number in [line.strip() for line in text_file.readlines()]]
    return input_lines

def is_safe(inputs_list):
    direction = 0
    for index, digit in enumerate(inputs_list):
        change = 0

        first_number = int(digit)
        try:
            second_number = int(inputs_list[index + 1])
        except IndexError:
            change += first_number
            break
        change += first_number - second_number

        if not -3 <= change <= 3 or change == 0:
            return False

        if change > 0:
            direction += 1
        elif change == 0 and index > 1:
            if int(inputs_list[index - 1]) > 0:
                direction += 1
                continue
            direction -= 1
        else:
            direction -= 1

    return abs(direction) ==  len(inputs_list) - 1

if __name__ == '__main__':
    lines = get_inputs()

    result = 0
    for line_ in lines:
        if is_safe(line_):
            result += 1
    print(result)