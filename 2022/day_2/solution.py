ROCK_SCORE = 1
PAPER_SCORE = 2
SCISSORS_SCORE = 3

LOSS_SCORE = 0
DRAW_SCORE = 3
WIN_SCORE = 6


def part_one():
    scores = {
        'A': ROCK_SCORE,
        'X': ROCK_SCORE,
        'B': PAPER_SCORE,
        'Y': PAPER_SCORE,
        'C': SCISSORS_SCORE,
        'Z': SCISSORS_SCORE
    }

    win_table = {
        'Z': 'B',
        'X': 'C',
        'Y': 'A',
    }

    draw_table = {
        'X': 'A',
        'Y': 'B',
        'Z': 'C',
    }

    # Read input and store mad strats
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
        rules = [(move.split()[0], move.split()[1],) for move in lines]

    total_score = 0
    for rule in rules:
        total_score += scores[rule[1]]
        total_score += DRAW_SCORE if rule[0] == draw_table[rule[1]] else (WIN_SCORE if rule[0] == win_table[rule[1]] else LOSS_SCORE)  # noqa: E501

    return total_score


def part_two():
    scores = {
        'A': [SCISSORS_SCORE, ROCK_SCORE, PAPER_SCORE],
        'B': [ROCK_SCORE, PAPER_SCORE, SCISSORS_SCORE],
        'C': [PAPER_SCORE, SCISSORS_SCORE, ROCK_SCORE]
    }

    rule_scores = {
        'X': LOSS_SCORE,
        'Y': DRAW_SCORE,
        'Z': WIN_SCORE
    }

    # Read input and store mad strats
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
        rules = [(move.split()[0], move.split()[1],) for move in lines]

    total_score = 0
    for rule in rules:
        win_condition_score = rule_scores[rule[1]]
        total_score += win_condition_score
        total_score += scores[rule[0]][int(win_condition_score / 3)]

    return total_score
