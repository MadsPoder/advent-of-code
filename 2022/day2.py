from functools import reduce


with open ('day2.txt') as fp:
    strategy_guide = [tuple(x.strip('\n').split(' ')) for x in fp.readlines()]

SCORE_X = 1
SCORE_Y = 2
SCORE_Z = 3

WIN = 6
LOSS = 0
DRAW = 3

# A = X = 1 = Rock
# B = Y = 2 = Paper
# C = Z = 3 = Scissors
def calculate_score(input: tuple[str, str]) -> int:
    match input:
        case ('A', 'X'): return SCORE_X + DRAW # Draw
        case ('A', 'Y'): return SCORE_Y + WIN  # Win
        case ('A', 'Z'): return SCORE_Z + LOSS # Loss

        case ('B', 'X'): return SCORE_X + LOSS # Loss
        case ('B', 'Y'): return SCORE_Y + DRAW # Draw
        case ('B', 'Z'): return SCORE_Z + WIN  # Win

        case ('C', 'X'): return SCORE_X + WIN  # Win
        case ('C', 'Y'): return SCORE_Y + LOSS # Loss
        case ('C', 'Z'): return SCORE_Z + DRAW # Draw

# Part 1 sum scores
print(reduce(lambda previous, current: previous + calculate_score(current), strategy_guide, 0))

# X = We need to loose
# Y = We need to draw
# Z = We need to win
def calculate_score_part_2(input: tuple[str, str]) -> int:
    match input:
        case ('A', 'X'): return SCORE_Z + LOSS # We need to loose (Z)
        case ('A', 'Y'): return SCORE_X + DRAW # We need to draw (X)
        case ('A', 'Z'): return SCORE_Y + WIN  # We need to win (Y)

        case ('B', 'X'): return SCORE_X + LOSS # We need to loose (X)
        case ('B', 'Y'): return SCORE_Y + DRAW # We need to draw (Y)
        case ('B', 'Z'): return SCORE_Z + WIN # We need to win (Z)

        case ('C', 'X'): return SCORE_Y + LOSS # We need to loose (Y)
        case ('C', 'Y'): return SCORE_Z + DRAW # We need to draw (Z)
        case ('C', 'Z'): return SCORE_X + WIN # We need to win (X)

# Part 2 sum scores
print(reduce(lambda previous, current: previous + calculate_score_part_2(current), strategy_guide, 0))