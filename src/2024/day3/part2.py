from pathlib import Path
import re

def get_data():
    data_path = Path(__file__).parent.parent.joinpath("inputs/day3.txt")
    with data_path.open("r") as data_:
        return data_.read()

def get_pattern(data):
    pattern = r"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))"
    expressions = re.findall(pattern, "".join(data))

    enabled = True
    result = 0

    for expression in expressions:
        match expression[0]:
            case "do()":
                enabled = True
            case "don't()":
                enabled = False
            case _ if enabled:
                result += int(expression[1]) * int(expression[2])

    return result

if __name__ == '__main__':
    input_data = get_data()
    print(get_pattern(input_data))
