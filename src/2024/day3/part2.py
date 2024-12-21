from pathlib import Path

CLEAN_LIST = []

def get_data():
    data_path = Path(__file__).parent.parent.joinpath("inputs/day3.txt")
    with data_path.open("r") as data_:
        return data_.read()

def multiply():
    result_ = 0
    for item in CLEAN_LIST:
        values = item.split(",")
        result_ += int(values[0]) * int(values[1])
    return result_

def clean_up(data):
    global CLEAN_LIST

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

        CLEAN_LIST.append(data[index_ + 4: next_parentheses])
        index_ += 1

def get_pattern(data):
    state = False
    starting_point = 0
    while True:
        try:
            do_index = data.index("do()", starting_point)
            dont_index = data.index("don't()", starting_point)
        except ValueError:
            break

        nearest = do_index if dont_index > do_index else dont_index

        if starting_point > nearest:
            state = True

        if not state:
            clean_up(data[starting_point:nearest])
            starting_point += nearest
            continue

        clean_up(data[do_index:dont_index])
        starting_point = dont_index + 1

if __name__ == '__main__':
    input_data = get_data()
    get_pattern(input_data)
    result = multiply()
    print(result)