from typing import Optional

# Read puzzle input
with open ('input.txt') as fp:
    data = [int(line.strip()) for line in fp.readlines()]

def find_pair_sum_value(data: list[int], sum_value: int) -> Optional[tuple[int, int]]:
    state = set()

    # Should be O(N) single traversel required
    for i in data:
        val = sum_value - i  # subtract ith element from expected value
        if val in state:  # if this value is in the set, ith and val will be the pair
            return val, i
        state.add(i)  # add i to the state set
