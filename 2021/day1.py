import functools

# Read puzzle input
with open ('day1.txt') as fp:
    depth_measurements = [int(x) for x in fp.readlines()]

# In the pursuit of unreadable one-liners
larger_than_previous = lambda x: functools.reduce(lambda res, el: res + 1 if (x[el[0] - 1] < el[1]) and el[0] != 0 else res + 0, enumerate(x), 0)

# Part 1
print(larger_than_previous(depth_measurements))

# Part 2
N = 3
sliding_window = [depth_measurements[i:i+N] for i in range(len(depth_measurements) - N + 1)]
filtered_depth_measurement = list(map(lambda x: sum(x), sliding_window))

print(larger_than_previous(filtered_depth_measurement))