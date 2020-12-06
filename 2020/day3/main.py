# Read puzzle input
with open ('input.txt') as fp:
    data = [x.strip() for x in fp.readlines()]

def n_trees_hit_on_slope(slope: list[str], right: int, down: int) -> int:
    n_trees = 0
    n = len(slope)
    i = 0  # x position on slope
    idx = 0  # y position on slope

    # Good old imperative solution
    while idx <= n:

        # Move along the slope
        i += right  # move x
        idx += down  # move y
        
        # Break if we hit the bottom
        if idx > n - down:
            break

        # Length of line 
        length = len(data[idx])
        
        # Increment counter if hit a tree
        n_trees += 1 if data[idx][i % length] == '#' else 0

    return n_trees

n_trees_part_1 = n_trees_hit_on_slope(data, 3, 1)

print(n_trees_part_1)

n_trees_part_2 = \
n_trees_hit_on_slope(data, 1, 1) * \
n_trees_hit_on_slope(data, 3, 1) * \
n_trees_hit_on_slope(data, 5, 1) * \
n_trees_hit_on_slope(data, 7, 1) * \
n_trees_hit_on_slope(data, 1, 2)

print(n_trees_part_2)