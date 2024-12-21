from pathlib import Path

INPUT_PATH = Path(__file__).parent.parent.joinpath("inputs/day1.txt")

if __name__ == '__main__':
    with INPUT_PATH.open("r") as text_file:
        numbers = text_file.read().split()

    right_digits = []
    left_digits = []

    for index, digit in enumerate(numbers):
        if index % 2 == 0:
            left_digits.append(int(digit))
            continue
        right_digits.append(int(digit))

    result = 0
    for digit in left_digits:
        result += digit * right_digits.count(digit)

    print(result)
