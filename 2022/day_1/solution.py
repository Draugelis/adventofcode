def part_one():
    # Read file
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()

    # Collect calory data
    calories = []
    elf = 0
    for row in lines:
        if not row:
            calories.append(elf)
            elf = 0
            continue
        elf += int(row)

    # Find elf with the most calories
    max_cal = max(calories)
    return max_cal


def part_two():
    # Read file
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()

    # Collect calory data
    calories = []
    elf = 0
    for row in lines:
        if not row:
            calories.append(elf)
            elf = 0
            continue
        elf += int(row)

    # Find 3 elves with the most calories
    return sum(sorted(calories, reverse=True)[:3])
