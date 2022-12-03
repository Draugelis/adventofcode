def item_priority(item):
    # Lower case leters have 1-26 range and upper case have 27-52
    return ord(item) - 96 if item.islower() else ord(item) - 38


def find_match(first, second):
    for item in first:
        if item in second:
            return item


def find_common_item(first, second, third):
    first_matches = [x for x in first if x in second]
    common_item = [x for x in first_matches if x in third]
    return common_item[0]


def part_one():
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()

    total_priority = 0
    for item_list in lines:
        first = item_list[:int(len(item_list)/2)]
        second = item_list[int(len(item_list)/2):]
        shared_item = find_match(first, second)
        total_priority += item_priority(shared_item)

    return total_priority


def part_two():
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()

    total_priority = 0
    for i in range(0, len(lines), 3):
        common_item = find_common_item(lines[i], lines[i+1], lines[i+2])
        total_priority += item_priority(common_item)

    return total_priority
