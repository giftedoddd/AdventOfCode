from pathlib import Path

def get_data():
    data_path = Path(__file__).parent.parent.joinpath("inputs/day3.txt")
    with data_path.open("r") as data_:
        return data_.read()

def multiply(items: list):
    result_ = 0
    for item in items:
        values = item.split(",")
        result_ += int(values[0]) * int(values[1])
    return result_

def clean_up(data):
    clean = []

    index_ = 0
    while True:
        try:
            index_ = data.index("mul", index_)
        except ValueError:
            break

        if not data[index_ + 3] == "(":
            index_ += 1
            continue

        next_comma = data.index(",", index_)
        if not data[index_ + 4:next_comma].isdigit():
            index_ += 1
            continue

        next_parentheses = data.index(")", index_)
        if not data[next_comma + 1:next_parentheses].isdigit():
            index_ += 1
            continue

        clean.append(data[index_ + 4: next_parentheses])
        index_ += 1

    return clean

if __name__ == '__main__':
    data_data = get_data()
    safe_list = clean_up(data_data)
    result = multiply(safe_list)
    print(result)