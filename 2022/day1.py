from heapq import heapify, nlargest
from itertools import groupby
from functools import reduce


with open ('day1.txt') as fp:
    calories_input = [x.strip("\n") for x in fp.readlines()]

# Group into list of lists - list for each elf
calories_per_elf = [
    list(
        [int(calorie) for calorie in calories_for_elf]
    ) for delimiter, calories_for_elf in groupby(calories_input, key = lambda x: x == '') if not delimiter
]

# Sum each list per elf
total_calories_per_elf = [
    reduce(lambda previous, current: previous + current, elf) for elf in calories_per_elf
]

# Convert into heap
heapify(total_calories_per_elf)

# Part 1. Get max number
# Using max here, but it should just be heap.max
print(max(total_calories_per_elf))

# Part 2. Get sum of 3 largest calories
print(
    reduce(lambda previous, current: previous + current, nlargest(3, total_calories_per_elf))
)
