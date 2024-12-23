from pathlib import Path

def get_input():
    input_path = Path(__file__).parent.parent.joinpath("inputs/day5.txt")
    with input_path.open("r") as _:
        return _.read().split("\n")

def parse_input(data:list):
    seperator = data.index("")
    page_orders = [x.split("|") for x in data[:seperator]]
    page_updates = ["".join(y) for y in data[seperator + 1:]]
    return page_orders, page_updates

def main():
    raw_input = get_input()
    page_orders, page_updates = parse_input(raw_input)

if __name__ == '__main__':
    main()