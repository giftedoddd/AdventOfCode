with open("inputs/day1.txt") as file:
    numbers = file.read().split()

if __name__ == '__main__':
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