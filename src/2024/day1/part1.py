from pathlib import Path

INPUT_PATH = Path(__file__).parent.parent.joinpath("inputs/day1.txt")

if __name__ == '__main__':
    with INPUT_PATH.open("r") as file:
        numbers = file.read().split()

    right_digits = []
    left_digits = []

    for index, digit in enumerate(numbers):
        if index % 2 == 0:
            left_digits.append(int(digit))
            continue
        right_digits.append(int(digit))

    right_digits.sort()
    left_digits.sort()

    result = 0
    for l_digit, r_digit in zip(left_digits, right_digits):
        result += abs(l_digit - r_digit)
    print(result)
